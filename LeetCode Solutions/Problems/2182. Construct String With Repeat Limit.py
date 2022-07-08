class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        lst = sorted(list(s), reverse=True)
        count = 1
        j = 0
        for i in range(1, len(lst)):
            if lst[i-1] == lst[i]:
                count += 1
                if count > repeatLimit:
                    j = max(j, i+1)
                    while j < len(lst):
                        if lst[j] != lst[i]:
                            lst[j], lst[i] = lst[i], lst[j]
                            count=1
                            break
                        j += 1
                    if j >= len(lst):
                        return ''.join(lst[:i])
            else:
              count = 1
        return ''.join(lst)