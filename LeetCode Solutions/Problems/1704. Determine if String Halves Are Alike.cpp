string vowels = "AEIOUaeiou";
class Solution {
public:
    bool halvesAreAlike(string s) {
        int middle = s.size() / 2, result = 0;
        for(int i=0, j=middle; i<middle; i++, j++){
            if(~vowels.find(s[i])){
                result++;
            }
            if(~vowels.find(s[j])){
                result--;
            }
        }
        return result == 0;
    }
};