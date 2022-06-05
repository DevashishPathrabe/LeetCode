class Solution {
    public int scoreOfParentheses(String S) {
        int power = 0, score = 0;
        for (int i=1; i<S.length(); i++){
            if (S.charAt(i) == '('){
                power++;
            }
            else if (S.charAt(i-1) == '('){
                score += 1 << power--;
            } else{
                power--;
            }
        }
        return score;
    }
}