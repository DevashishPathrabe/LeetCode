class Solution {
public:
    int minFlips(string target) {
        int flips = 0;
        for (const auto &bit: target){
            if (flips%2 - (bit-'0') != 0){
                flips++;
            }
        }
        return flips;
    }
};