class Solution:
    def calculateMaxInfoGain(self, petal_length: List[float], species: List[str]) -> float:
        def entropy(lst):
            n = len(lst)
            P = [f/n for f in Counter(lst).values()]
            H = -sum([p * math.log(p, 2) for p in P])
            return H
        
        def info_gain(lst,lst1,lst2):
            return entropy(lst) - len(lst1)/len(lst)*entropy(lst1) - len(lst2)/len(lst)*entropy(lst2)
        
        data = sorted(zip(petal_length, species), key=lambda x: x[0])
        sorted_species = [x[1] for x in data]
        
        max_gain = 0.0
        for i in range(len(data)):
            max_gain = max(max_gain, info_gain(sorted_species, sorted_species[:i], sorted_species[i:]))
        return max_gain