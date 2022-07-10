class Solution {
    public String findLongestWord(String s, List<String> dictionary) {
        String longestString = "";
        for(String word : dictionary){
            int wordLength = word.length(), stringLength = longestString.length();
            if(wordLength < stringLength || (wordLength == stringLength && word.compareTo(longestString) > 0)){
                continue;
            }
            int position = -1;
            for(int i=0; i<wordLength; i++){
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