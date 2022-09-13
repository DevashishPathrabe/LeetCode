class Solution {
    public int minNumberOfHours(int initialEnergy, int initialExperience, int[] energy, int[] experience) {
        int answer = 0;
        for (int i=0;i<energy.length;i++){
            if (initialEnergy <= energy[i]){
                answer += energy[i]-initialEnergy+1;
                initialEnergy = 1;
            }
            else{
                initialEnergy = initialEnergy-energy[i];
            }
            if (initialExperience <= experience[i]){
                answer += experience[i]-initialExperience+1;
                initialExperience = experience[i]+1;
            }
            initialExperience = experience[i]+initialExperience;
        }
        return answer;
    }
}