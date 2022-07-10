class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        result = 0
        ipv4 = queryIP.split('.')
        if len(ipv4) == 4:
            for x in ipv4:
                if x == '' or (x[0] == '0' and len(x) != 1) or not x.isdigit() or int(x) > 255:
                    result = 1
                    break
            if not result:
                return 'IPv4'
        ipv6 = queryIP.split(':')
        if len(ipv6) == 8:
            for x in ipv6:
                if x == '' or len(x) > 4 or not all(c in hexdigits for c in x):
                    result = 1
                    break
            if not result:
                return 'IPv6'
        return 'Neither'