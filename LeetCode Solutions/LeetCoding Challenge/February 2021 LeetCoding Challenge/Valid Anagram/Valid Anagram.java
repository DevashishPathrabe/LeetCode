class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length())
            return false;
        int[] count = new int[26];
        int len = s.length();
        for (int i=0; i<len; i++){
            count[s.charAt(i)-'a']++;
            count[t.charAt(i)-'a']--;
        }
        for (int i=0; i<26; i++){
            if (count[i]!=0)
                return false;
        }
        return true;
    }
}