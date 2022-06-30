class Solution {
    public int scoreOfParentheses(String s) {
        int power = 0, score = 0;
        for (int i=1; i<s.length(); i++){
            if (s.charAt(i) == '('){
                power++;
            }
            else if (s.charAt(i-1) == '('){
                score += 1 << power--;
            } else{
                power--;
            }
        }
        return score;
    }
}