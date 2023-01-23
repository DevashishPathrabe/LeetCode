class Solution {
public:
    int minimumRounds(vector<int>& tasks) {
        unordered_map<int, int> count;
        int result = 0, freq1;
        for (int a: tasks){
            ++count[a];
        }
        for (auto& it: count){
            if (it.second == 1){
                return -1;
            }
            result += (it.second + 2) / 3;
        }
        return result;
    }
};