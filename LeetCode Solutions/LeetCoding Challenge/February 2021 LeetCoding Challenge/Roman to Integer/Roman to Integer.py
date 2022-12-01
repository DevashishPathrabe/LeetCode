class Solution:
    def romanToInt(self, s: str) -> int:
        integer = 0
        roman = None
        for i in s:
            if (i == 'M'):
                if (roman == 'C'):
                    integer += 800
                else:
                    integer += 1000
            elif (i == 'D'):
                if (roman == 'C'):
                    integer += 300 
                else:
                    integer += 500
            elif (i == 'C'):
                if (roman == 'X'):
                    integer += 80 
                else:
                    integer += 100
            elif (i == 'L'):
                if (roman == 'X'):
                    integer += 30 
                else:
                    integer += 50
            elif (i == 'X'):
                if (roman == 'I'):
                    integer += 8 
                else:
                    integer += 10
            elif (i == 'V'):
                if (roman == 'I'):
                    integer += 3 
                else:
                    integer += 5
            else:
                integer += 1
            roman = i
        return integer