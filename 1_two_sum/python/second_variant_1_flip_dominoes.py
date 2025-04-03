from collections import defaultdict


class Solution:
    def flipDominoesTrick(self, dominoes: list[list[int]], target: int) -> int:
        domino_freq = defaultdict(int)
        result = 0
        for domino in dominoes:
            a1, a2 = domino
            b1, b2 = target - a1, target - a2
            b = b1 * 10 + b2
            result += domino_freq[b]
            domino_freq[a1 * 10 + a2] += 1
        return result

    def flipDominoes(self, dominoes: list[list[int]], target: int) -> int:
        seen = defaultdict(int)
        for domino in dominoes:
            seen[tuple(domino)] += 1

        result = 0
        unique_pairs = list(seen.keys())
        for pair in unique_pairs:
            a, b = pair
            if (target - a, target - b) in seen:
                complement = (target - a, target - b)
                if complement == pair:
                    result += seen[pair] * (seen[pair] - 1) // 2
                else:
                    result += seen[complement] * seen[pair]
                    seen.pop(complement)
                seen.pop(pair)
        return result


if __name__ == "__main__":
    solution = Solution()
    assert (
        solution.flipDominoes(
            [[3, 4], [1, 9], [3, 4], [2, 1], [9, 1], [9, 1], [7, 6], [1, 9]], 10
        )
        == 6
    )
    assert solution.flipDominoes([[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], 0) == 10
    assert (
        solution.flipDominoesTrick(
            [[3, 4], [1, 9], [3, 4], [2, 1], [9, 1], [9, 1], [7, 6], [1, 9]], 10
        )
        == 6
    )
    assert solution.flipDominoesTrick([[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], 0) == 10
