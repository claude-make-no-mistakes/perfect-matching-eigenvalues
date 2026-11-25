"""Check lower-order sufficient conditions against the pinned authors' workbook."""

import argparse
from fractions import Fraction
import json
from pathlib import Path

from check_n8 import workbook_bytes, workbook_sheet
from exact_quotient import valency


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workbook", type=Path, help="local copy of the pinned workbook")
    options = parser.parse_args()
    content = workbook_bytes(options.workbook)
    matrices = {n: workbook_sheet(content, n)[0] for n in range(2, 16)}
    one_singleton_count = 0
    zero_singleton_failures = []
    for s in range(2, 15):
        threshold = Fraction(3 * s + 4, 2 * (s + 1) * (s + 2))
        for singleton_count in (0, 1):
            size = s + singleton_count
            matrix = matrices[size]
            for relation, degree in matrix[size,].items():
                if relation.count(1) != singleton_count:
                    continue
                assert degree == valency(relation)
                largest, label = max((value[relation], shape) for shape, value in matrix.items()
                                     if shape != (size,))
                signed = Fraction(largest, degree)
                if singleton_count:
                    assert signed < threshold
                    one_singleton_count += 1
                elif signed > threshold:
                    zero_singleton_failures.append({
                        "core": relation, "maximizer": label, "signed": str(signed),
                        "threshold": str(threshold),
                    })

    print(json.dumps({"one_singleton_checks": one_singleton_count,
                      "zero_singleton_failures": zero_singleton_failures}, indent=2))


if __name__ == "__main__":
    main()
