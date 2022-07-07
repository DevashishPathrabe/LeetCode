class Solution {
public:
    int addRungs(vector<int>& rungs, int dist) {
        int previous = 0, minimumNumberOfRungs = 0;
        for(int r:rungs){
            minimumNumberOfRungs += (r-previous-1) / dist;
            previous = r;
        }
        return minimumNumberOfRungs;
    }
};