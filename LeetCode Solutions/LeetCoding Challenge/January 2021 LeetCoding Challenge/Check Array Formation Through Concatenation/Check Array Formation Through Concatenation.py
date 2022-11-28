class Solution(object):
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        i = 0
        count = 0
        while (i < len(pieces)):
            for j in range(len(arr)):
                if (arr[j:j+len(pieces[i])] == pieces[i]):
                    count += 1
                    break
            i += 1
        if (count == len(pieces)):
            return True
        else:
            return False