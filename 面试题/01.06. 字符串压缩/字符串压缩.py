#!/usr/bin/python3

class Solution:
    def compressString(self, S: str) -> str:
        if not S:
            return S

        if len(S) == 1:
            return S

        first, second = 0, 1
        ans = ''

        while second < len(S):
            if S[first] == S[second]:
                second += 1
            else:
                ans += (S[first] + str(second - first))
                first = second
                second += 1

        ans += (S[first] + str(second - first))

        if len(S) <= len(ans):
            return S

        return ans