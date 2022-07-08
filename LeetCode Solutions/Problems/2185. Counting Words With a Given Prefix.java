class Solution {
    public int prefixCount(String[] words, String pref) {
        int numberOfStrings = 0;
        for(String w: words) 
            numberOfStrings += (w.indexOf(pref) == 0) ? 1 : 0;
        return numberOfStrings;
    }
}