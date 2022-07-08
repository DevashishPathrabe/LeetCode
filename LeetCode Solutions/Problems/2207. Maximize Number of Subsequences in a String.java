class Solution {
    public long maximumSubsequenceCount(String text, String pattern) {
        long result = 0, count1 = 0, count2 = 0;
        for (int i = 0; i < text.length(); ++i) {   
            if (text.charAt(i) == pattern.charAt(1)) {   
                result += count1;
                count2++;
            }
            if (text.charAt(i) == pattern.charAt(0)) {   
                count1++;
            }
        }
        return result + Math.max(count1, count2);
    }
}