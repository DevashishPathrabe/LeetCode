class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        dict = {}
        for a, b in knowledge:
            dict[a] = b
        result, temp  = '', ''
        isopened = False
        for i in range(len(s)):
            if s[i] == '(':
                isopened = True
            elif s[i] == ')':
                key = temp
                if key in dict:
                    result = result + dict[key]
                else:
                    result = result + '?'
                temp = ''
                isopened = False
            elif  isopened == False:
                result = result + s[i]
            elif isopened == True:
                temp = temp + s[i]
        return result