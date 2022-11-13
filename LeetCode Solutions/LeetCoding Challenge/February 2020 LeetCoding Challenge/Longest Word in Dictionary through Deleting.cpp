class Solution {
public:
    string findLongestWord(string s, vector<string>& d) {
        string longestString = "";
        for(string word : d){
            int a = word.length(), b = longestString.length();
            if(a < b || (a == b && word > longestString)){
                continue;
            }
            int position = -1;
            for(int i=0; i<a; i++){
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