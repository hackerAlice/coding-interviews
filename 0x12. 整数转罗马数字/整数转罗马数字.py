class Solution:
    def intToRoman(self, num: int) -> str:
        roman_chars = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        numbers = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

        # special_transfer = {
        #     4: 'IV',
        #     9: "IX",
        #     40: 'XL',
        #     90: 'XC',
        #     400: 'CD',
        #     900: 'CM'
        # }

        # if num in special_transfer:
        #     return special_transfer[num]

        index = len(roman_chars) - 1
        ans = ''
        while num > 0:
            if num >= numbers[index]:
                ans += (roman_chars[index] * (num // numbers[index]))
                num %= numbers[index]
            index -= 1

        return ans
