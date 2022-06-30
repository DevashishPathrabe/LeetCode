class Solution {
public:
    int scoreOfParentheses(string s) {
        int power = 0, score = 0;
        for (int i=1; i<s.length(); i++){
            if (s[i] == '('){
                power++;
            }
            else if (s[i-1] == '('){
                score += 1 << power--;
            } else{
                power--;
            }
        }
        return score;
    }
};