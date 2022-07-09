class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        resultString = []
        for i in range(1, n+1):
            if(i%3 == 0 and i%5 == 0):
                resultString.append('FizzBuzz')
            elif(i%5 == 0):
                resultString.append('Buzz')
            elif(i%3 == 0):
                resultString.append('Fizz')
            else:
                resultString.append(str(i))
        return resultString