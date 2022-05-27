class Solution {
public:
    int maxPower(string s) {
        int count = 1;
        int power = 1;
        for (int i=0; i<s.size() - 1; i++){
            if (s[i] == s[i+1]){
                count++;
            } else{
                count = 1;
            }
            power = max(power, count);
        }
        return power;
    }
};