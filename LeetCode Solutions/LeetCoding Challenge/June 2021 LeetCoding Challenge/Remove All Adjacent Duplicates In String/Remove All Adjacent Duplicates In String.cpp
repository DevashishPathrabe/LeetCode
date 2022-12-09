class Solution {
public:
    string removeDuplicates(string s) {
        string finalString = "";
        for (char c : s){
            if (!finalString.empty() && finalString.back() == c){
                finalString.pop_back();
            } else{
                finalString.push_back(c);
            }
        }
        return finalString;
    }
};