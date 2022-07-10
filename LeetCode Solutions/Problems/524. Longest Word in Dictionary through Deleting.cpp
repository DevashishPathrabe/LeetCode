class Solution {
public:
    string findLongestWord(string s, vector<string>& dictionary) {
        string longestString = "";
        for(string word : dictionary){
            int wordLength = word.length(), stringLength = longestString.length();
            if(wordLength < stringLength || (wordLength == stringLength && word > longestString)){
                continue;
            }
            int position = -1;
            for(int i=0; i<wordLength; i++){
                position = s.find(word[i], position + 1);
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
};