#!/usr/bin/python3

class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        return len(s1) == len(s2) and sorted(s1) == sorted(s2)