class Solution:
    def myAtoi(self, s: str) -> int:
        e = re.search(r"^[-+]?\d+", s.lstrip())
        if(e):
            return max(min(int(e.group(0)), 2**31-1), -2**31)
        else:
            return 0