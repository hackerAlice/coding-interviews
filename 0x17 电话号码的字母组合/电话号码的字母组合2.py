"""
使用辅助队列
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 对应数字字符和字母的映射
        d = {
            '2': ('a', 'b', 'c'),
            '3': ('d', 'e', 'f'),
            '4': ('g', 'h', 'i'),
            '5': ('j', 'k', 'l'),
            '6': ('m', 'n', 'o'),
            '7': ('p', 'q', 'r', 's'),
            '8': ('t', 'u', 'v'),
            '9': ('w', 'x', 'y', 'z'),
        }

        if not digits:
            return []

        q = ['']

        for digit in digits:
            for _ in range(len(q)):
                temp = q.pop(0)
                for letter in d[digit]:
                        q.append(temp+letter)

        return q