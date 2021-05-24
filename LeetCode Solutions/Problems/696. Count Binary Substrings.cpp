class Solution {
public:
    int countBinarySubstrings(string s) {
        int current = 1, previous = 0, result = 0;
        for(int i=1; i<s.length(); i++){
            if(s[i] == s[i-1]){
                current++;
            } else{
                result += min(current, previous), previous = current, current = 1;
            }
        }
        return result + min(current, previous);
    }
};