class Solution {
public:
    int minSetSize(vector<int>& arr) {
        unordered_map<int, int> count;
        for(int x : arr){
            ++count[x];
        }
        vector<int> frequencies;
        for(auto [_, freq] : count){
            frequencies.push_back(freq);
        }
        sort(frequencies.begin(), frequencies.end());
        int minimumSize = 0, removed = 0, half = arr.size() / 2, i = frequencies.size() - 1;
        while(removed < half){
            minimumSize += 1;
            removed += frequencies[i--];
        }
        return minimumSize;
    }
};