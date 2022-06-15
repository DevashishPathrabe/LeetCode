class Solution {
    public String findLongestWord(String s, List<String> d) {
        String longestString = "";
        for(String word : d){
            int a = word.length(), b = longestString.length();
            if(a < b || (a == b && word.compareTo(longestString) > 0)){
                continue;
            }
            int position = -1;
            for(int i=0; i<a; i++){
                position = s.indexOf(word.charAt(i), position + 1);
                if(position == -1){
                    break;
                }
            }
            if(position != -1){
                longestString = word;
            }
        }
        return longestString;
    }
}