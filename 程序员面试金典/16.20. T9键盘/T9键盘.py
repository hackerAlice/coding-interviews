#!/usr/bin/python3

from typing import List


class Solution:
    def getValidT9Words(self, num: str, words: List[str]) -> List[str]:
        d = {
            '2': list('abc'),
            '3': list('def'),
            '4': list('ghi'),
            '5': list('jkl'),
            '6': list('mno'),
            '7': list('pqrs'),
            '8': list('tuv'),
            '9': list('wxyz'),
        }

        res = []

        for word in words:
            i = 0
            while i < len(word):
                if word[i] not in d[num[i]]:
                    break
                i += 1
            if i == len(word):
                res.append(word)

        return res


if __name__ == "__main__":
    print(Solution().getValidT9Words("2", ["a", "b", "c", "d"]))