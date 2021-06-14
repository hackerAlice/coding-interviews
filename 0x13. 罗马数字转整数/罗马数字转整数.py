class Solution:
    def romanToInt(self, s: str) -> int:
        roman_chars = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        numbers = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

        d = dict(zip(roman_chars, numbers))

        if len(s) <= 1:
            return d[s]
        result = 0

        i = 0
        while i < len(s):
            j = i + 1
            if j < len(s) and s[i:j+1] in ['IV', 'IX', "XL", "XC", "CD", "CM"]:
                result += d[s[i:j+1]]
                i += 2
            else:
                result += d[s[i]]
                i += 1

        return result
