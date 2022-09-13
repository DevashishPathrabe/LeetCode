class Solution {
public:
    int minimumRecolors(string blocks, int k) {
        int answer = INT_MAX;
        int n = blocks.size();
        for (int i=0;i+k<=n;++i){
            int slidingStart = i;
            int slidingEnd = i + k;
            int blackCount = 0;
            while (slidingStart < slidingEnd) {
                if (blocks[slidingStart] == 'B'){
                    ++blackCount;
                }
                ++slidingStart;
            }
            answer = min(answer, k - blackCount);
        }
        return answer;
    }
};