from collections import defaultdict
class ThroneInheritance:
    def __init__(self, kingName: str):
        self.dead = set()
        self.kingdom = defaultdict(list)
        self.root = kingName
        
    def birth(self, parentName: str, childName: str) -> None:
        self.kingdom[parentName].append(childName)
        
    def death(self, name: str) -> None:
        self.dead.add(name)
        
    def getInheritanceOrder(self) -> List[str]:
        result = []
        def dfs(root):
            if root not in self.dead:
                result.append(root)
            for nxt in self.kingdom[root]:
                dfs(nxt)
        dfs(self.root)
        return result
# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()