class Solution {
public:
    int prefixCount(vector<string>& words, string pref) {
        int numberOfStrings = 0;
        for(string w: words) 
            numberOfStrings += w.find(pref) == 0;
        return numberOfStrings;
    }
};