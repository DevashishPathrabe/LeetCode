class Solution {
public:
    int minNumberOfHours(int initialEnergy, int initialExperience, vector<int>& energy, vector<int>& experience) {
        int count=0;
        for (int i=0;i<energy.size();i++){
            if (energy[i] >= initialEnergy){
                while (initialEnergy <= energy[i]){
                    initialEnergy++;
                    count++;
                }
            }
            if (experience[i] >= initialExperience){
                while (initialExperience <= experience[i]){
                    initialExperience++;
                    count++;
                }
            }
            initialExperience += experience[i];
            initialEnergy -= energy[i];
        }
        return count;
    }
};