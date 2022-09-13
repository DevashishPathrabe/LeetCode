class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        currentEnergy = initialEnergy
        currentExperience = initialExperience
        answer = 0
        for i in range(len(energy)):
            if currentExperience <= experience[i]:
                answer += experience[i] - currentExperience+1
                currentExperience = experience[i]+1
            if currentEnergy <= energy[i]:
                answer += energy[i] - currentEnergy + 1
                currentEnergy = energy[i]+1
            currentEnergy -= energy[i]
            currentExperience += experience[i]
        return answer