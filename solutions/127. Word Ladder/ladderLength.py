"""LeetCode 127: Word Ladder.

Problem summary:
Return the number of words in the shortest valid one-letter-at-a-time
transformation from ``beginWord`` to ``endWord``, or zero if none exists.

Source: https://leetcode.com/problems/word-ladder/
"""


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        unused = set(wordList)
        if endWord not in unused:
            return 0

        front = {beginWord}
        back = {endWord}
        unused.discard(beginWord)
        unused.discard(endWord)
        length = 1

        while front and back:
            if len(front) > len(back):
                front, back = back, front

            next_front: set[str] = set()
            for word in front:
                for index, original in enumerate(word):
                    for letter_code in range(ord("a"), ord("z") + 1):
                        letter = chr(letter_code)
                        if letter == original:
                            continue
                        candidate = word[:index] + letter + word[index + 1 :]
                        if candidate in back:
                            return length + 1
                        if candidate in unused:
                            next_front.add(candidate)

            unused.difference_update(next_front)
            front = next_front
            length += 1

        return 0


if __name__ == "__main__":
    solution = Solution()
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    assert solution.ladderLength("hit", "cog", words) == 5
    assert solution.ladderLength("hit", "cog", words[:-1]) == 0
    assert solution.ladderLength("a", "c", ["a", "b", "c"]) == 2
    print("All tests passed.")
