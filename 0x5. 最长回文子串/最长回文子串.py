#!/usr/bin/python3

"""
使用动态规划
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length < 2:
            return s
        begain, max_len = 0, 1
        # dp[i][j] 表示 s[i..j] 是否是回文串
        dp = [[False] * length for _ in range(length)]
        for i in range(length):
            dp[i][i] = True

        # 递推开始
        # 先枚举子串长度
        for L in range(2, length+1):
            # 枚举左边界，左边界的上限设置可以宽松一些
            for i in range(length):
                j = i+L-1

                # 如果右边界越界，就可以退出当前循环
                if j >= length:
                    break

                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]

                # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begain = i

        return s[begain:begain+max_len]


if __name__ == "__main__":
    assert "bab" == Solution().longestPalindrome("babad")
