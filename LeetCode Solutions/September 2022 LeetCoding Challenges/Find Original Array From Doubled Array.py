class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2:
            return []
        changed.sort()
        hashmap = {}
        for num in changed:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        original = []
        for key in hashmap:
            if key == 0:
                for _ in range(1, hashmap[key], 2):
                    original.append(0)
            elif hashmap[key] != 0:
                if key * 2 in hashmap:
                    if hashmap[key] > hashmap[key * 2]:
                        return []
                    elif hashmap[key] < hashmap[key * 2]:
                        hashmap[key * 2] = hashmap[key * 2] - hashmap[key]
                        for _ in range(hashmap[key]):
                            original.append(key)
                        hashmap[key] = 0
                    else:
                        for _ in range(hashmap[key]):
                            original.append(key)
                        hashmap[key] = 0
                        hashmap[key * 2] = 0
                else:
                    return []
        return original