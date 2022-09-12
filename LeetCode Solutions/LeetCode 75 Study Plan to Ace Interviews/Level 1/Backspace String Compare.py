class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def final_string(s):
            index = 0
            final = ""
            while index < len(s):
                if s[index] == '#':
                    if len(final) > 0:
                        final = final[:-1]
                else:
                    final += s[index]
                index += 1
            return final
        if final_string(s) == final_string(t):
            return True
        else:
            return False