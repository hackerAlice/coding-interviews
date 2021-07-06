#!/usr/bin/python3

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return

        prefix = strs[0]

        for i in range(1, len(strs)):
            prefix = self._lcp(prefix, strs[i])
            if not prefix:
                break
        return prefix

    def _lcp(self, str1, str2):
        """
        求两个字符串的公共前缀
        """
        length, index = min(len(str1), len(str2)), 0

        while index < length and str1[index] == str2[index]:
            index += 1

        return str1[:index]

