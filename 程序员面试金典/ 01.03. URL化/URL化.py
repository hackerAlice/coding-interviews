#!/usr/bin/python3

class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        ans = ''
        for i in range(length):
            if S[i] == " ":
                ans += "%20"
            else:
                ans += S[i]

        return ans