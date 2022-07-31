class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        unordered_map<int, int> set;
        for (int i : arr) {
            if (set[2*i] > 0 || ((i%2 == 0) && (set[i/2] > 0))){
                return true;
            }
            set[i]++;
        }
        return false;
    }
};