"""LeetCode 126: Word Ladder II.

Problem summary:
Return every shortest sequence from ``beginWord`` to ``endWord`` in which
each step changes one letter and every later word belongs to ``wordList``.

Source: https://leetcode.com/problems/word-ladder-ii/
"""

from collections import defaultdict


class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: list[str]
    ) -> list[list[str]]:
        unused = set(wordList)
        if endWord not in unused:
            return []

        parents: dict[str, list[str]] = defaultdict(list)
        current_level = {beginWord}
        unused.discard(beginWord)
        found = False

        while current_level and not found:
            next_level: set[str] = set()

            for word in current_level:
                for index, original in enumerate(word):
                    for letter_code in range(ord("a"), ord("z") + 1):
                        letter = chr(letter_code)
                        if letter == original:
                            continue
                        candidate = word[:index] + letter + word[index + 1 :]
                        if candidate not in unused:
                            continue

                        parents[candidate].append(word)
                        next_level.add(candidate)
                        if candidate == endWord:
                            found = True

            unused.difference_update(next_level)
            current_level = next_level

        if not found:
            return []

        result: list[list[str]] = []
        stack = [(endWord, [endWord])]
        while stack:
            word, reverse_path = stack.pop()
            if word == beginWord:
                result.append(reverse_path[::-1])
                continue
            for parent in parents[word]:
                stack.append((parent, reverse_path + [parent]))

        return result


if __name__ == "__main__":
    solution = Solution()
    actual = solution.findLadders(
        "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]
    )
    expected = {
        ("hit", "hot", "dot", "dog", "cog"),
        ("hit", "hot", "lot", "log", "cog"),
    }
    assert {tuple(path) for path in actual} == expected
    assert solution.findLadders(
        "hit", "cog", ["hot", "dot", "dog", "lot", "log"]
    ) == []
    print("All tests passed.")
