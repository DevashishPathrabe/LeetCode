class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left = 1
        right = (position[-1]-position[0])//(m-1)
        while (left <= right):
            mid = left + (right-left)//2
            valid = True
            k = m-1
            i = 0
            while (i < len(position) and k > 0):
                index = bisect_left(position, position[i]+mid)
                if index >= len(position):
                    valid = False
                    break
                i = index
                k-=1
            if valid:
                left = mid+1
            else:
                right = mid-1
        return right