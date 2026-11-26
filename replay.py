"""Replay all exact computational certificates. Run with Python 3.12+ and SymPy 1.14."""

import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory


HERE = Path(__file__).resolve().parent


def read_json(path):
    return json.loads(path.read_bytes())


def run(script, *args):
    result = subprocess.run(
        [sys.executable, "-E", "-B", str(HERE / script), *map(str, args)],
        cwd=HERE, stdout=subprocess.PIPE, text=True, check=True,
    )
    return result.stdout


def require_same(actual, expected, label):
    if actual != expected:
        raise ValueError(f"Replayed output differs from the archived {label}")


def verify_hashes(manifest, folder):
    for record in manifest.read_text(encoding="utf-8").splitlines():
        expected, relative = record.split(maxsplit=1)
        actual = sha256((folder / relative).read_bytes()).hexdigest()
        require_same(actual, expected, relative)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workbook", type=Path, help="local copy of the hash-pinned authors' workbook")
    parser.add_argument("--cxx", help="path to a C++17 compiler")
    args = parser.parse_args()
    verify_hashes(HERE / "matchings/baseline/SHA256SUMS", HERE / "matchings")
    workbook = args.workbook.resolve() if args.workbook else None
    if workbook is None:
        cached = HERE / "workbook.xlsx"
        if cached.is_file():
            workbook = cached
    # Fetch the pinned input once when running outside the original workspace.
    sys.path.insert(0, str(HERE / "matchings"))
    from check_n8 import workbook_bytes
    msys = Path("C:/msys64/ucrt64/bin/g++.exe")
    compiler = args.cxx or (str(msys) if os.name == "nt" and msys.is_file() else shutil.which("g++"))
    if not compiler:
        parser.error("a C++17 compiler is required; set --cxx to its path")
    compiler = shutil.which(compiler) or compiler
    os.environ["PATH"] = str(Path(compiler).parent) + os.pathsep + os.environ["PATH"]
    with TemporaryDirectory() as staging:
        local_input = Path(staging) / "published.xlsx"
        local_input.write_bytes(workbook_bytes(workbook))
        baseline = json.loads(run("matchings/check_baseline.py"))
        require_same(baseline, read_json(HERE / "matchings/baseline/baseline.json"), "matching baseline")
        computed = Path(staging) / "orbit.json"
        run("matchings/check_n8.py", "--cxx", compiler, "--workbook", local_input, "--output", computed)
        require_same(read_json(computed), read_json(HERE / "matchings/certificate_n8.json"), "orbit spectra")
        print("Matching orbit enumeration and 484 labelled eigenvalues reproduced.", flush=True)
        lower = json.loads(run("matchings/check_stretch.py", "--workbook", local_input))
        require_same(lower["one_singleton_checks"], 134, "one-singleton count")
        require_same(sorted(tuple(case["core"]) for case in lower["zero_singleton_failures"]),
                     [(2, 2), (2, 2, 2), (2, 2, 2, 2), (3, 3)], "zero-singleton exceptions")
        print("All 134 one-singleton bounds and four zero-singleton failures reproduced.", flush=True)
        print(run("verification/verify_bases.py", "--workbook", local_input).strip(), flush=True)


if __name__ == "__main__":
    main()
