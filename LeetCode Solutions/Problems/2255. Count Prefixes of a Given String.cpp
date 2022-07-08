class Solution {
public:
    int countPrefixes(vector<string>& words, string s) {
        int result = 0;
        for (auto& w : words)
            result += s.find(w) < 1;
        return result;
    }
};