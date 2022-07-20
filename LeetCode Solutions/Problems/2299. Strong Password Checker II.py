class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) >= 8:
            special = ['!','@','#','$','%','^','&','*',')','(','-','+']
            hasUpper, hasLower, hasNum, hasSpecial = False, False, False, False
            for i in range(len(password)):
                if i < len(password)-1 and password[i] == password[i+1]:
                    return False
                if password[i] in special:
                    hasSpecial = True
                if password[i].isupper():
                    hasUpper = True
                if password[i].islower():
                    hasLower = True
                if password[i].isdigit():
                    hasNum = True
            return hasUpper and hasLower and hasNum and hasSpecial