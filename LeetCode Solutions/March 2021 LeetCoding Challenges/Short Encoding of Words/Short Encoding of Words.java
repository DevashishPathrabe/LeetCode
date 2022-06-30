class Solution {
    public int minimumLengthEncoding(String[] words) {
        Set<String> wordsSet = new HashSet<>(Arrays.asList(words));
        for (String word : words){
            if (wordsSet.contains(word)){
                for (int i=1; i<word.length(); i++){ 
                    wordsSet.remove(word.substring(i));
                }
            }
        }
        int lengthOfTheShortestReferenceString = wordsSet.size();
        for (String word : wordsSet){
            lengthOfTheShortestReferenceString += word.length();
        }
        return lengthOfTheShortestReferenceString;
    }
}