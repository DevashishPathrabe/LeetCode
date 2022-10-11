class Solution {
public:
    int maxProduct(vector<string>& words) {
        int maximumValue = 0;
        vector<int> bitsets(words.size());
        for(int i=0; i<words.size(); i++){
            string& word = words[i];
            int bitset = 0;
            for(char& c : word){
                bitset |= 1 << (c - 'a');
            }
            for(int j=0; j<i; j++){
                if((bitsets[j] & bitset) == 0){
                    maximumValue = max(maximumValue, int(word.length() * words[j].length()));
                }
            }
            bitsets[i] = bitset;
        }
        return maximumValue;
    }
};