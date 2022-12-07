class Solution {
    public int longestStrChain(String[] words) {
        List<Set<String>> W = new ArrayList<>(17);
        for (int i=0; i<17; i++){
            W.add(new HashSet<>());
        }
        for (String word : words){
            W.get(word.length()).add(word);
        }
        Map<String, Integer> arr = new HashMap<>();
        int longestPossibleLength = 1;
        for (int i=16; i>0; i--){
            if (W.get(i-1).isEmpty()){
                continue;
            }
            for (String word : W.get(i)){
                int wordValue = arr.getOrDefault(word, 1);
                for (int j=0; j<word.length(); j++){
                    String predecessors = word.substring(0,j) + word.substring(j+1);
                    if (W.get(i-1).contains(predecessors) && wordValue >= arr.getOrDefault(predecessors,1)){
                        arr.put(predecessors, wordValue + 1);
                        longestPossibleLength = Math.max(longestPossibleLength, wordValue + 1);
                    }
                }
            }
        }
        return longestPossibleLength;
    }
}