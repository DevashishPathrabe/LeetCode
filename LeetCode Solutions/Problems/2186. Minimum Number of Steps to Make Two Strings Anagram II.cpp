class Solution {
public:
    int minSteps(string s, string t) {
        int minNumberOfSteps = 0;
        vector<int> sCounter(26, 0), tCounter(26, 0);
        for (char ch: s){
            sCounter[ch - 'a']++;
        }
        for (char ch: t){
            tCounter[ch - 'a']++;
        }
        for (int i=0; i<26; i++){
            minNumberOfSteps += abs(sCounter[i] - tCounter[i]);
        }
        return minNumberOfSteps;
    }
};