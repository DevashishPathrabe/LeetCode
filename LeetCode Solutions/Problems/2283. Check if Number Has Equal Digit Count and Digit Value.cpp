class Solution {
public:
    bool digitCount(string num) {
        const size_t totalDigits = 10;
        array<int, totalDigits> frequency{};
        for (int i=0; i<num.length(); ++i){
            frequency[num[i] - '0']++;
        }
        for (int i=0; i<num.length(); ++i){
            if (frequency[i] != (num[i] - '0')){
                return false;
            }
        }
        return true;
    }
};