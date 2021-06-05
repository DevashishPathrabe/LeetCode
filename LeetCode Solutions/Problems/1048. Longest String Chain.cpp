class Solution {
public:
    int longestStrChain(vector<string>& words) {
        vector<unordered_set<string>> W(17);
        for(auto word : words){
            W[word.size()].insert(word);
        }
        unordered_map<string, int> arr;
        int longestPossibleLength = 1;
        for(int i=16; i; i--){
            if(W[i-1].empty()){
                continue;
            }
            for(auto word : W[i]){
                int wordValue = arr[word] ? arr[word] : 1;
                for(int j=0; j<word.size(); j++){
                    string predecessors = word.substr(0,j) + word.substr(j+1);
                    int predecessorsValue = arr[predecessors] ? arr[predecessors] : 1;
                    if(W[i-1].find(predecessors) != W[i-1].end() && wordValue >= predecessorsValue){
                        arr[predecessors] = wordValue + 1;
                        longestPossibleLength = max(longestPossibleLength, wordValue + 1);
                    }
                }
            }
        }
        return longestPossibleLength;
    }
};