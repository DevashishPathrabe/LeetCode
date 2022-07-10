class Solution {
    public String longestWord(String[] words) {
        Arrays.sort(words);
        Set<String> set = new HashSet<String>();
        String former="";
        for (String w : words){
            if (w.length() == 1 || set.contains(w.substring(0, w.length() - 1))){
                former = w.length() > former.length() ? w : former;
                set.add(w);
            }
        }
        return former;
    }
}