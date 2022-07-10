class Solution {
public:
    string longestWord(vector<string>& words) {
        sort(words.begin(), words.end());
        unordered_set<string> ust;
        string former;
        for (auto &w : words){
            if (w.size() == 1 || ust.count(w.substr(0, w.size() - 1))){
                former = w.size() > former.size() ? w : former;  
                ust.insert(w);
          }
        }
        return former;
    }
};