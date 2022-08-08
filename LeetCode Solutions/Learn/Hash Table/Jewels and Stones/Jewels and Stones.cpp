class Solution {
public:
    int numJewelsInStones(string J, string S) {
        int result = 0;
        for (int i=0; i<S.length(); i++){
            if (J.find(S[i]) < J.length()){
                result++;
            }
        }
        return result;
    }
};