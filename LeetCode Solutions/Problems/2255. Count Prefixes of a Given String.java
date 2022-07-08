class Solution {
    public int countPrefixes(String[] words, String s) {
        int result = 0;
        for (String w : words)
            if (s.startsWith(w))
                result++;
        return result;
    }
}