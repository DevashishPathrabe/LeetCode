class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            position_of_at = s.find('@')
            s = s.lower()
            return s[0] + '*****'+s[position_of_at-1:].lower()
        else:
            s = "".join(i for i in s if i.isdigit())
            if len(s) == 10:
                return '***-***-' + s[-4:]
            elif len(s) == 11:
                return '+*-***-***-' + s[-4:]
            elif len(s) == 12:
                return "+**-***-***-" + s[-4:]
            elif len(s) == 13:
                return '+***-***-***-' + s[-4:]