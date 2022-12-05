class Solution {
public:
    int minimumLengthEncoding(vector<string>& words) {
        unordered_set<string> wordsSet(words.begin(), words.end());
        for (string word : words){
            if (wordsSet.find(word) != wordsSet.end()){
                for (int i=1; i<word.length(); i++){ 
                    wordsSet.erase(word.substr(i));
                }
            }
        }
        int lengthOfTheShortestReferenceString = wordsSet.size();
        for (string word : wordsSet){
            lengthOfTheShortestReferenceString += word.size();
        }
        return lengthOfTheShortestReferenceString;
    }
};