class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        numberOfAddress = []
        for email in emails:
            email = email.split('@')
            temp = email[0].split('+')
            temp[0] = temp[0].replace('.','')     
            email = '@'.join([temp[0],email[1]])
            if(email not in numberOfAddress):
                numberOfAddress.append(email)
        return len(numberOfAddress)