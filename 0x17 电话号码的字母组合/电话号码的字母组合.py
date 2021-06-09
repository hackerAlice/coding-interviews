#!/usr/bin/python3
"""
使用递归法
"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # 对应数字字符和字母的映射
        d = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']}

        result = []

        def backtrack(combination, nextdigit):
            if len(nextdigit) == 0:
                result.append(combination)
            else:
                for letter in d[nextdigit[0]]:
                    backtrack(combination+letter, nextdigit[1:])

        backtrack('', digits)

        return result


if __name__ == "__main__":
    Solution().letterCombinations('23')