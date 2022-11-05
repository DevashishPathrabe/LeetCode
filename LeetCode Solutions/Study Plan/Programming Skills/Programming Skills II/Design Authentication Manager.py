class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.tokens={}
        self.timeTolive=timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId]=(currentTime,currentTime+self.timeTolive)

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens:
            token_start,token_end=self.tokens[tokenId]
            if currentTime>=token_end:
                self.tokens.pop(tokenId)
            else:
                self.tokens[tokenId]=(currentTime,currentTime+self.timeTolive)

    def countUnexpiredTokens(self, currentTime: int) -> int:
        unexpired=0
        for token in self.tokens:
            if self.tokens[token][1]>currentTime:
                unexpired+=1
        return unexpired


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)