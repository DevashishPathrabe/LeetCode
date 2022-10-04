class Solution {
    public boolean isSubsequence(String s, String t) {
        int s_i = 0, t_i = 0;
        while (s_i < s.length() && t_i < t.length()){
            if (s.charAt(s_i) == t.charAt(t_i)){
                s_i++;
            }
            t_i++;
        }
        return s_i == s.length();
    }
}