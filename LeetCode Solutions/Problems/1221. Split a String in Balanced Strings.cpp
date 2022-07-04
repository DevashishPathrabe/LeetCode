class Solution {
public:
    int balancedStringSplit(string s) {
        int result = 0, count = 0;
        for (int i=0; i<s.size(); i++){
            if (s[i] == 'L'){
                count--;
            }
            else{
                count++;
            }
            if (count == 0){
                result++;
            }
        }
        return result;
    }
};