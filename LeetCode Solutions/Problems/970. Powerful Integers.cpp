class Solution {
public:
    vector<int> powerfulIntegers(int x, int y, int bound) {
        unordered_set<int> listOfPowerfullIntegers;
        for(int xi=1; xi<bound; xi*=x){
            for(int yj=1; xi+yj<=bound; yj*=y){
                listOfPowerfullIntegers.insert(xi+yj);
                if(y == 1){
                    break;
                }
            }
            if(x == 1){
                break;
            }
        }
        return vector<int>(listOfPowerfullIntegers.begin(), listOfPowerfullIntegers.end());
    }
};