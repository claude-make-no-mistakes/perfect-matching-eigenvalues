"""Exact perfect-matching eigenvalues from Jack orthogonality at alpha=2."""

import argparse
import json
from collections import Counter
from functools import cache
from math import factorial, gcd, lcm, prod
from pathlib import Path


def partitions(total, cap=None):
    if not total:
        yield ()
        return
    for first in range(min(total, cap or total), 0, -1):
        for tail in partitions(total - first, first):
            yield (first, *tail)


@cache
def labelled_monomial(parts):
    """Sum over distinct variable indices, expressed in power sums."""
    if not parts:
        return {(): 1}
    first, rest = parts[0], parts[1:]
    coefficients = Counter()
    for power, value in labelled_monomial(rest).items():
        coefficients[tuple(sorted((first, *power), reverse=True))] += value
    # The new index can collide with exactly one of the distinct old indices.
    for i, exponent in enumerate(rest):
        merged = (*rest[:i], first + exponent, *rest[i + 1 :])
        coefficients.subtract(labelled_monomial(tuple(sorted(merged, reverse=True))))
    return dict(coefficients)


def power_norm(part):
    return 2 ** len(part) * prod(
        exponent**count * factorial(count) for exponent, count in Counter(part).items()
    )


def dimension(part):
    shape = [2 * x for x in part]
    hooks = (
        width - j + sum(lower > j for lower in shape[i + 1 :])
        for i, width in enumerate(shape) for j in range(width)
    )
    return factorial(sum(shape)) // prod(hooks)


def dot(u, v):
    return sum(x * y for x, y in zip(u, v, strict=True))


def eigenmatrix(n):
    # Ascending lexicographic order extends ascending dominance order.
    parts = sorted(partitions(n))
    weights = [power_norm(p) for p in parts]
    rows, duals, norms = [], [], []
    for shape in parts:
        expansion = labelled_monomial(shape)
        vector = [expansion.get(p, 0) for p in parts]
        projections = []
        scale = 1
        for row, dual, norm in zip(rows, duals, norms, strict=True):
            numerator = dot(vector, dual)
            if numerator:
                common = gcd(numerator, norm)
                denominator = norm // common
                projections.append((row, numerator // common, denominator))
                scale = lcm(scale, denominator)
        vector = [scale * x for x in vector]
        for row, numerator, denominator in projections:
            multiple = numerator * (scale // denominator)
            vector = [v - multiple * u for v, u in zip(vector, row, strict=True)]
        # p_(1^n) is the identity relation and has eigenvalue one.
        divisor = vector[0]
        if divisor == 0 or any(x % divisor for x in vector):
            raise ArithmeticError(f"Invalid zonal normalization at {shape}")
        row = [x // divisor for x in vector]
        dual = [x * w for x, w in zip(row, weights, strict=True)]
        rows.append(row)
        duals.append(dual)
        norms.append(dot(row, dual))
    return parts, rows


def examine(n):
    parts, rows = eigenmatrix(n)
    target = parts.index((n - 1, 1))
    dims = [dimension(p) for p in parts]
    count = prod(range(1, 2 * n, 2))
    order = factorial(n) * 2**n
    if sum(dims) != count or sum(rows[-1]) != count:
        raise ArithmeticError("Multiplicity or valency total failed")
    bases = []
    for mu, column in zip(parts, zip(*rows, strict=True), strict=True):
        val = column[-1]
        if val * power_norm(mu) != order or sum(d * a*a for d, a in zip(dims, column)) != count * val:
            raise ArithmeticError(f"Valency or trace failed at {mu}")
        moved = n - mu.count(1)
        if (val - column[target]) * 2*n*(n-1) != val * moved*(2*n-1):
            raise ArithmeticError(f"Edge eigenvalue failed at {mu}")
        if mu.count(1) == 2:
            rival = max(column[i] for i in range(len(parts)-1) if i != target)
            bases.append({"core": list(mu[:-2]), "degree": val, "target": column[target],
                          "largest_competitor": rival, "gap": column[target] - rival})
    return {"n": n, "partitions": len(parts), "two_singleton_bases": bases}


def controls():
    p3, rows3 = eigenmatrix(3)
    assert rows3 == [[1,-3,2],[1,1,-2],[1,6,8]] and p3[1] == (2, 1)
    p4, rows4 = eigenmatrix(4)
    j = p4.index((3, 1))
    assert rows4[p4.index((3, 1))][j] < max(row[j] for row in rows4[:-1])
    assert all(row[0] == 1 for row in rows4)
    examine(3)
    examine(4)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--through", type=int)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    controls()
    if args.through is None:
        print("Exact n=3 spectrum, n=4 exception, identity ties and trace controls passed.")
        return
    if args.through < 4:
        parser.error("--through must be at least 4")
    data = [examine(n) for n in range(4, args.through + 1)]
    out = json.dumps(data, indent=2) + "\n"
    if args.output:
        args.output.write_bytes(out.encode())
    else:
        print(out, end="")


if __name__ == "__main__":
    main()
