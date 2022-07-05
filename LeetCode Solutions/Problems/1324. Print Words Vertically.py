class Solution:
    def printVertically(self, s: str) -> List[str]:
        return [''.join(col).rstrip() for col in itertools.zip_longest(*s.split(), fillvalue=' ')]