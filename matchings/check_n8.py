"""Build the orbit quotients, certify their spectra, and compare a pinned workbook."""

import argparse
from ast import literal_eval
from decimal import Decimal
from hashlib import sha256
from io import BytesIO
import json
from pathlib import Path
import re
import subprocess
from tempfile import TemporaryDirectory
from urllib.request import urlopen
from xml.etree import ElementTree
from zipfile import ZipFile

from sympy import Matrix

from exact_quotient import (
    certify_quotients, partitions, representation_key, small_quotients, target_result, valency,
)


COMMIT = "9bfd0192a04b1c271b305ee3c8146b356ac41603"
REPOSITORY = "https://raw.githubusercontent.com/Himanshugupta23/Perfect-Matching-Association-Scheme"
WORKBOOK = f"{REPOSITORY}/{COMMIT}/Excel_format_Evals_of_PM_Schm_upto_n=15.xlsx"
WORKBOOK_HASH = "0c6fa2980600f847844877c65324791be7c42ac89c4f70c9325e4bf749936eaa"
TARGETS = [(6, 1, 1), (4, 2, 1, 1), (3, 3, 1, 1), (2, 2, 2, 1, 1)]
MAIN_NS = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
REL_NS = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"


def native_quotients(executable, n):
    output = subprocess.check_output([executable, str(n)], text=True)
    size_data, *rows = [list(map(int, line.split())) for line in output.splitlines()]
    count = size_data[1]
    shapes = list(partitions(n))
    assert size_data == [n, len(shapes), sum(map(valency, shapes))]
    assert rows[:count] == [[len(shape), *shape] for shape in shapes]
    data = rows[count:]
    assert len(data) == count**2 and all(len(row) == count for row in data)
    return shapes, {shape: Matrix(data[index * count : (index + 1) * count])
                    for index, shape in enumerate(shapes)}


def workbook_bytes(path):
    if path:
        content = path.read_bytes()
    else:
        with urlopen(WORKBOOK, timeout=30) as response:
            content = response.read()
    assert sha256(content).hexdigest() == WORKBOOK_HASH
    return content


def doubled_shape(label):
    doubled = literal_eval(label)
    assert isinstance(doubled, list) and all(part >= 2 and part % 2 == 0 for part in doubled)
    return tuple(part // 2 for part in doubled)


def workbook_sheet(content, n):
    with ZipFile(BytesIO(content)) as archive:
        sheets = ElementTree.fromstring(archive.read("xl/workbook.xml")).find(f"{MAIN_NS}sheets")
        sheet_id = next(sheet.get(f"{REL_NS}id") for sheet in sheets if sheet.get("name") == f"n={n}")
        links = ElementTree.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
        member = next(link.get("Target") for link in links if link.get("Id") == sheet_id)
        strings = ElementTree.fromstring(archive.read("xl/sharedStrings.xml"))
        shared = ["".join(node.text or "" for node in text.iter(f"{MAIN_NS}t")) for text in strings]
        table = ElementTree.fromstring(archive.read(f"xl/{member}")).find(f"{MAIN_NS}sheetData")

    rows = []
    for row in table:
        cells = {}
        for cell in row:
            value = cell.findtext(f"{MAIN_NS}v")
            if value is not None:
                column = re.fullmatch(r"([A-Z]+)\d+", cell.get("r")).group(1)
                kind = cell.get("t", "n")
                if kind == "s":
                    cells[column] = shared[int(value)]
                elif kind == "n":
                    cells[column] = Decimal(value)
        if cells:
            rows.append(cells)

    header, *rows = rows
    row_label = next(column for column, label in header.items() if label == "Representation")
    dimension_col = next(column for column, label in header.items() if label == "Dimension")
    relations = {column: doubled_shape(label) for column, label in header.items()
                 if isinstance(label, str) and label.startswith("[")}
    values = {}
    dimensions = {}
    for row in rows:
        if row_label not in row:
            continue
        shape = doubled_shape(row[row_label])
        assert shape not in values
        values[shape] = {}
        for column, relation in relations.items():
            value = row[column]
            assert value == int(value)
            values[shape][relation] = int(value)
        dimension = row[dimension_col]
        assert dimension == int(dimension)
        dimensions[shape] = int(dimension)
    assert set(values) == set(relations.values()) == set(partitions(n))
    return values, dimensions


def main():
    args = argparse.ArgumentParser(description=__doc__)
    args.add_argument("--cxx", default="g++", help="path to the GNU C++17 compiler")
    args.add_argument("--workbook", type=Path, help="local copy of the pinned workbook")
    args.add_argument("--output", type=Path, help="path for the computed certificate")
    options = args.parse_args()
    with TemporaryDirectory() as temporary:
        executable = str(Path(temporary) / "orbit_quotients.exe")
        source = Path(__file__).with_name("orbit_quotients.cpp")
        subprocess.run([options.cxx, "-O3", "-std=c++17", "-Wall", "-Wextra", "-Wpedantic",
                        str(source), "-o", executable], check=True)
        for n in (3, 4):
            assert native_quotients(executable, n) == small_quotients(n)
        shapes, quotients = native_quotients(executable, 8)
    computed = certify_quotients(shapes, quotients)
    source_spectra, source_dimensions = workbook_sheet(workbook_bytes(options.workbook), 8)
    assert computed == source_spectra
    assert source_dimensions == {shape: representation_key(shape)[0] for shape in shapes}

    results = [dict(relation=relation, **target_result(computed, relation)) for relation in TARGETS]
    assert all(result["accepted"] for result in results)
    output = {
        "n": 8,
        "matchings": sum(map(valency, shapes)),
        "native_quotients_verified_against_python_at": [3, 4],
        "worksheet_entries_verified": len(shapes) ** 2,
        "worksheet_dimensions_verified": len(shapes),
        "workbook_commit": COMMIT,
        "workbook_sha256": WORKBOOK_HASH,
        "shape_order": shapes,
        "base_results": results,
        "eigenvalue_table": [[computed[shape][column] for column in shapes] for shape in shapes],
    }
    rendered = json.dumps(output, indent=2) + "\n"
    if options.output:
        options.output.write_text(rendered, encoding="utf-8", newline="\n")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
