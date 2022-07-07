class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        vector<string> result;
        if (s.length() <= 10){
            return result;
        }
        map<string,int> m;
        for (int i=0; i<=s.length()-10; i++){
            string k = s.substr(i, 10);
            m[k]++;
        }
        for (auto i:m){
            if (i.second > 1){
                result.push_back(i.first);
            }
        }
        return result;
    }
};