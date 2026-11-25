"""Replay the two-singleton base certificates and compare to published spectra."""

import argparse
import json
import sys
from hashlib import sha256
from pathlib import Path

from zonal import controls, eigenmatrix, examine


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "matchings"))
from check_n8 import workbook_bytes, workbook_sheet


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workbook", type=Path, help="local copy of the authors' pinned workbook")
    args = parser.parse_args()
    frozen_hash = "229872eaa7d33df45d84a8f57293612776781ff4497edfda3e6469b9c130a57f"
    if sha256((HERE / "zonal.py").read_bytes()).hexdigest() != frozen_hash:
        raise ValueError("The zonal checker differs from the version frozen at baseline")
    controls()
    records = json.loads((HERE / "two-singleton-bases.json").read_bytes())
    if records != [examine(n) for n in range(4, 19)]:
        raise ValueError("Base data differs from an independent full regeneration")
    bases = [entry for record in records for entry in record["two_singleton_bases"]]
    if len(bases) != 230 or any(entry["gap"] <= 0 for entry in bases):
        raise ValueError("Core coverage or strict inequality failed")
    workbook = workbook_bytes(args.workbook)
    entries = 0
    for n in range(4, 16):
        published, _ = workbook_sheet(workbook, n)
        parts, rows = eigenmatrix(n)
        for part, row in zip(parts, rows, strict=True):
            if row != [published[part][mu] for mu in parts]:
                raise ValueError(f"Published spectrum differs at n={n}, shape={part}")
            entries += len(row)
    print(f"Reproduced {len(bases)} strictly positive base gaps and {entries} published eigenvalues.")


if __name__ == "__main__":
    main()
