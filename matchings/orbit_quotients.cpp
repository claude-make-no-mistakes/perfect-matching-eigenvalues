#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <stdexcept>
#include <vector>

// Enumerate each matching once. For a fixed reference and one representative
// of each reference orbit, accumulate counts indexed by both pair types.
using Matching = std::array<int, 16>;
using Partition = std::vector<int>;
using Mask = std::uint32_t;

void partitions(int remaining, int maximum, Partition& prefix,
                std::vector<Partition>& result) {
    if (remaining == 0) {
        result.push_back(prefix);
        return;
    }
    for (int part = std::min(remaining, maximum); part >= 1; --part) {
        prefix.push_back(part);
        partitions(remaining - part, part, prefix, result);
        prefix.pop_back();
    }
}

Matching representative(const Partition& shape) {
    Matching matching{};
    int start = 0;
    for (int part : shape) {
        for (int edge = 0; edge < part; ++edge) {
            const int right = start + 2 * edge + 1;
            const int left = start + 2 * ((edge + 1) % part);
            matching[left] = right;
            matching[right] = left;
        }
        start += 2 * part;
    }
    return matching;
}

// A sum of four-bit increments encodes the multiplicities of cycle parts.
std::uint32_t part_code(int part) {
    return std::uint32_t{1} << ((part - 1) * 4);
}

std::uint32_t type_code(const Matching& left, const Matching& right,
                        Mask uncovered) {
    std::uint32_t code = 0;
    while (uncovered != 0) {
        const int start = __builtin_ctz(uncovered);
        int vertex = start;
        int size = 0;
        do {
            const int middle = left[vertex];
            uncovered ^= (Mask{1} << vertex) | (Mask{1} << middle);
            vertex = right[middle];
            ++size;
        } while (vertex != start);
        code += part_code(size);
    }
    return code;
}

template <typename Visit>
void enumerate(Matching& matching, Mask unmatched, const Visit& visit) {
    if (unmatched == 0) {
        visit(matching);
        return;
    }
    const int first = __builtin_ctz(unmatched);
    unmatched ^= Mask{1} << first;
    for (Mask choices = unmatched; choices != 0; choices &= choices - 1) {
        const int second = __builtin_ctz(choices);
        matching[first] = second;
        matching[second] = first;
        enumerate(matching, unmatched ^ (Mask{1} << second), visit);
    }
}

int main(int argc, char** argv) {
    const int n = argc == 2 ? std::atoi(argv[1]) : 0;
    if (n < 2 || n > 8) {
        std::cerr << "usage: orbit_quotients N, with 2 <= N <= 8\n";
        return 2;
    }
    const Mask vertices = (Mask{1} << (2 * n)) - 1;
    std::vector<Partition> shapes;
    Partition prefix;
    partitions(n, n, prefix, shapes);
    const int count = static_cast<int>(shapes.size());
    std::vector<Matching> reps;
    std::vector<std::uint32_t> codes;
    std::uint32_t code_mask = 0;
    for (const auto& shape : shapes) {
        reps.push_back(representative(shape));
        std::uint32_t code = 0;
        for (int part : shape) {
            code += part_code(part);
        }
        codes.push_back(code);
        code_mask |= code;
    }
    // Pack only the bits used by valid partitions. On n=8 the table is tiny.
    auto pack = [code_mask](std::uint32_t code) {
        unsigned compact = 0;
        unsigned position = 0;
        for (std::uint32_t bits = code_mask; bits != 0; bits &= bits - 1) {
            const auto bit = bits & (-bits);
            compact |= static_cast<unsigned>((code & bit) != 0) << position;
            ++position;
        }
        return compact;
    };
    std::vector<int> indices(std::size_t{1} << __builtin_popcount(code_mask), -1);
    for (int index = 0; index < count; ++index) {
        indices[pack(codes[index])] = index;
    }
    std::vector counts(count, std::vector(count, std::vector<std::uint32_t>(count)));
    auto type_index = [&](const Matching& left, const Matching& right) {
        const int index = indices[pack(type_code(left, right, vertices))];
        if (index < 0) {
            throw std::logic_error("invalid alternating-cycle partition");
        }
        return index;
    };
    Matching current{};
    std::uint32_t total = 0;
    enumerate(current, vertices, [&](const Matching& matching) {
        ++total;
        const int column = type_index(reps.back(), matching);
        for (int row = 0; row < count; ++row) {
            const int relation = type_index(reps[row], matching);
            ++counts[relation][row][column];
        }
    });
    std::cout << n << ' ' << count << ' ' << total << '\n';
    for (const auto& shape : shapes) {
        std::cout << shape.size();
        for (int part : shape) {
            std::cout << ' ' << part;
        }
        std::cout << '\n';
    }
    for (const auto& quotient : counts) {
        for (const auto& row : quotient) {
            for (int col = 0; col < count; ++col) {
                std::cout << (col == 0 ? "" : " ") << row[col];
            }
            std::cout << '\n';
        }
    }
}
