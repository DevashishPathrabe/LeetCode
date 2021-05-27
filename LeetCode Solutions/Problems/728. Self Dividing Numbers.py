class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        output = []
        for i in range(left, right+1):
            number = i
            result = True
            while(number):
                modulus = number%10
                if(modulus==0 or i%modulus!=0):
                    result = False
                    break
                number //= 10
            if(result):
                output.append(i)
        return output