"""Reproduce the frozen positive and negative controls in exact arithmetic."""

import json

from exact_quotient import certify_quotients, small_quotients, target_result


# Gupta et al., arXiv:2510.17135v2, Appendix A, Tables 4 and 5.
PUBLISHED = {
    3: [[8, 6, 1], [-2, 1, 1], [2, -3, 1]],
    4: [[48, 32, 12, 12, 1], [-8, 4, -2, 5, 1], [-2, -8, 7, 2, 1],
        [4, -2, -2, -1, 1], [-6, 8, 3, -6, 1]],
}


def main():
    eigenvalues = {}
    for n, expected in PUBLISHED.items():
        shapes, quotients = small_quotients(n)
        eigenvalues[n] = certify_quotients(shapes, quotients)
        computed = [[eigenvalues[n][shape][column] for column in shapes] for shape in shapes]
        assert computed == expected

    positive = target_result(eigenvalues[4], (2, 1, 1))
    negative = target_result(eigenvalues[4], (3, 1))
    # Table 5 distinguishes signed and absolute order in the switch column.
    assert positive == dict(degree=12, target=5, accepted=True, maximizers=[[3, 1]],
                            signed_competitor=2, absolute_competitor=6)
    assert negative == dict(degree=32, target=4, accepted=False, maximizers=[[1, 1, 1, 1]],
                            signed_competitor=8, absolute_competitor=8)
    print(json.dumps({"published_tables_verified": [3, 4], "positive": positive,
                      "negative": negative}, indent=2))


if __name__ == "__main__":
    main()
