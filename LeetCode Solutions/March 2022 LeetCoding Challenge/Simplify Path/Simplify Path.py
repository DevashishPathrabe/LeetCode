class Solution:
    def simplifyPath(self, path: str) -> str:
        array = path.split('/')
        j = 1
        for i in array:
            if (i == '..'):
                j = max(1, j-1)
            elif (i and i != '.'):
                array[j] = i
                j += 1
        del array[j:]
        return '/'.join(array) or '/'