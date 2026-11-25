"""Exact counterexample search for Gupta et al., arXiv:2510.17135v2 §§1, 6."""

import argparse
import json
from math import prod

from zonal import controls, dimension, eigenmatrix


def inspect(n, *, diameter):
    shapes, matrix = eigenmatrix(n)
    columns = list(zip(*matrix, strict=True))
    dimensions = [dimension(shape) for shape in shapes]
    size = prod(range(1, 2 * n, 2))
    degrees = matrix[-1]
    if sum(dimensions) != size or sum(degrees) != size:
        raise ArithmeticError("Invalid representation dimensions or valencies")
    target = shapes.index((n - 1, 1))
    gaps = []
    signed_failures = []
    for relation, values in zip(shapes, columns, strict=True):
        degree = values[-1]
        if sum(d * value * value for d, value in zip(dimensions, values, strict=True)) != size * degree:
            raise ArithmeticError(f"Trace identity failed for {relation}")
        if relation == (1,) * n:
            continue
        best = max(values[:-1])
        gaps.append((degree - best, relation))
        if relation.count(1) >= 2 or relation == (n - 1, 1):
            if values[target] < best:
                signed_failures.append((relation, values[target], best))
    min_gap = min(gaps)
    distinguished = (2,) + (1,) * (n - 2)
    distinguished_gap = next(gap for gap, relation in gaps if relation == distinguished)

    no_walks = []
    if diameter:
        # (I+A)^k has positive coefficients at precisely the reached orbitals.
        # The trace pairing recovers each coefficient with denominator size*degree.
        for relation, values in zip(shapes[1:], columns[1:], strict=True):
            weights = [d * (1 + ev)**(n - 1) for d, ev in zip(dimensions, values, strict=True)]
            for other, degree, spherical in zip(shapes, degrees, columns, strict=True):
                numerator = sum(w * ev for w, ev in zip(weights, spherical, strict=True))
                if numerator % (size * degree) or numerator < 0:
                    raise ArithmeticError(f"Invalid walk coefficient at {relation}, {other}")
                if numerator == 0:
                    no_walks.append((relation, other))
    return {
        "n": n,
        "relations": len(shapes) - 1,
        "second_eigenvalue_failures": signed_failures,
        "minimum_gap": min_gap[0],
        "gap_minimizers": [relation for gap, relation in gaps if gap == min_gap[0]],
        "edge_switch_gap": distinguished_gap,
        "diameter_bound_failures": no_walks if diameter else None,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--through", type=int, default=18)
    parser.add_argument("--diameters-through", type=int, default=18)
    args = parser.parse_args()
    controls()
    for n in range(5, args.through + 1):
        print(json.dumps(inspect(n, diameter=n <= args.diameters_through)), flush=True)


if __name__ == "__main__":
    main()
