class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        int result = 0;
        for (int i=0; i<stones.length(); i++){
            if (jewels.find(stones[i]) < jewels.length()){
                result++;
            }
        }
        return result;
    }
};