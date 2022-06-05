class Solution {
public:
    int scoreOfParentheses(string S) {
        int power = 0, score = 0;
        for (int i=1; i<S.length(); i++){
            if (S[i] == '('){
                power++;
            }
            else if (S[i-1] == '('){
                score += 1 << power--;
            } else{
                power--;
            }
        }
        return score;
    }
};