value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""
        for i in range(13):
            while(num >= value[i]):
                roman += symbol[i]
                num -= value[i]
        return roman