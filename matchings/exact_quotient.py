"""Exact orbit quotients and simultaneous eigenspaces for perfect matchings."""

from collections import Counter
from itertools import product
from math import factorial, prod

from sympy import Matrix, Rational, eye


def partitions(total, maximum=None):
    if total == 0:
        yield ()
        return
    limit = total if maximum is None else min(total, maximum)
    for first in range(limit, 0, -1):
        for tail in partitions(total - first, first):
            yield (first,) + tail


def valency(shape):
    return 2 ** (sum(shape) - len(shape)) * factorial(sum(shape)) // prod(
        factorial(count) * part**count for part, count in Counter(shape).items()
    )


def matchings(n):
    partner = [-1] * (2 * n)

    def fill(unmatched):
        if not unmatched:
            yield tuple(partner)
            return
        first, *rest = unmatched
        for index, second in enumerate(rest):
            partner[first], partner[second] = second, first
            yield from fill(rest[:index] + rest[index + 1 :])

    yield from fill(list(range(2 * n)))


def pair_type(left, right):
    uncovered = set(range(len(left)))
    parts = []
    while uncovered:
        start = vertex = min(uncovered)
        size = 0
        while True:
            middle = left[vertex]
            uncovered.remove(vertex)
            uncovered.remove(middle)
            vertex = right[middle]
            size += 1
            if vertex == start:
                break
        parts.append(size)
    return tuple(sorted(parts, reverse=True))


def orbit_representative(shape):
    partner = [-1] * (2 * sum(shape))
    start = 0
    for part in shape:
        for edge in range(part):
            second = start + 2 * edge + 1
            first = start + 2 * ((edge + 1) % part)
            partner[first], partner[second] = second, first
        start += 2 * part
    return tuple(partner)


def small_quotients(n):
    shapes = list(partitions(n))
    root = orbit_representative((1,) * n)
    labeled = [(matching, pair_type(root, matching)) for matching in matchings(n)]
    quotients = {shape: [] for shape in shapes}
    for row in shapes:
        rep = orbit_representative(row)
        counts = Counter((pair_type(rep, matching), col) for matching, col in labeled)
        for relation in shapes:
            quotients[relation].append([counts[relation, col] for col in shapes])
    return shapes, {shape: Matrix(rows) for shape, rows in quotients.items()}


def representation_key(shape):
    widths = [2 * part for part in shape]
    hooks = []
    content_sum = 0
    for row, width in enumerate(widths):
        for col in range(width):
            hooks.append(width - col + sum(other > col for other in widths[row + 1 :]))
            content_sum += col - row
    dimension = factorial(sum(widths)) // prod(hooks)
    return dimension, content_sum


def certify_quotients(shapes, quotients):
    n = sum(shapes[0])
    size = len(shapes)
    degrees = [valency(shape) for shape in shapes]
    reference = shapes.index((1,) * n)
    switch = (2,) + (1,) * (n - 2)
    assert quotients[(1,) * n] == eye(size)
    left_weight = Matrix([degrees])
    diagonal = Matrix.diag(*degrees)
    all_entries = Matrix([degrees] * size)
    assert sum(quotients.values(), Matrix.zeros(size)) == all_entries
    for relation, matrix in quotients.items():
        assert matrix * Matrix.ones(size, 1) == valency(relation) * Matrix.ones(size, 1)
        assert left_weight * matrix == valency(relation) * left_weight
        assert diagonal * matrix == matrix.T * diagonal
        assert matrix[reference, shapes.index(relation)] == valency(relation)
    for left, right in product(quotients.values(), repeat=2):
        assert left * right == right * left

    spaces = [eye(size)]
    refinement_order = [switch] + [shape for shape in shapes if shape != switch]
    for relation in refinement_order:
        matrix = quotients[relation]
        refined = []
        for basis in spaces:
            if basis.cols == 1:
                refined.append(basis)
                continue
            restricted = basis.gauss_jordan_solve(matrix * basis)[0]
            for eigenvalue, _, vectors in restricted.eigenvects():
                assert eigenvalue.is_Integer
                refined.append(basis * Matrix.hstack(*vectors))
        spaces = refined
        if all(basis.cols == 1 for basis in spaces):
            break
    assert len(spaces) == size and all(basis.cols == 1 for basis in spaces)

    # The H-fixed spherical function has value 1 at the root after rescaling.
    # Orthogonality recovers the irrep dimension. The transposition sum is
    # n I + 2 A_switch and acts by the sum of diagram contents.
    labels = {representation_key(shape): shape for shape in shapes}
    assert len(labels) == size, "Dimension and transposition content do not separate these labels"
    eigenvalues = {}
    for vector in spaces:
        assert vector[reference] != 0
        vector = vector / vector[reference]
        norm = (vector.T * diagonal * vector)[0]
        dimension = sum(degrees) / norm
        row = {}
        for relation, quotient in quotients.items():
            image = quotient * vector
            value = image[reference]
            assert value.is_Integer and image == value * vector
            row[relation] = int(value)
        label = labels[(dimension, n + 2 * row[switch])]
        assert label not in eigenvalues
        eigenvalues[label] = row
    return {shape: eigenvalues[shape] for shape in shapes}


def target_result(eigenvalues, relation):
    n = sum(relation)
    target = (n - 1, 1)
    values = {shape: row[relation] for shape, row in eigenvalues.items() if shape != (n,)}
    competitors = {shape: value for shape, value in values.items() if shape != target}
    largest = max(values.values())
    target_value = values[target]
    s = n - relation.count(1)
    rho = 1 - Rational(s, 2) * (Rational(1, n) + Rational(1, n - 1))
    assert target_value == valency(relation) * rho
    return {
        "degree": valency(relation),
        "target": target_value,
        "accepted": target_value == largest,
        "maximizers": [list(shape) for shape, value in values.items() if value == largest],
        "signed_competitor": max(competitors.values()),
        "absolute_competitor": max(map(abs, competitors.values())),
    }
