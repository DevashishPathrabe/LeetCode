class Solution {
public:
    vector<int> pathInZigZagTree(int label) {
        int l = 1;
        while (label > pow(2, l)-1){
            ++l;
        }
        int i = label - pow(2,l-1);
        if (l % 2 == 0){
            i = pow(2, l-1)-1-i;
        }
        vector<int> result;
        for (int j=l; j>0; --j){
            if (j % 2){
                result.push_back(pow(2, j-1)+i);
            } else{
                result.push_back((pow(2,j)-1)-i);
            }
            i /= 2;
        }
        reverse(result.begin(),result.end());
        return result;
    }
};