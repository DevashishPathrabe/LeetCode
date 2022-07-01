class Solution {
public:
    vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
        sort(products.begin(), products.end());
        vector<vector<string>> List;
        int left = 0, right = products.size() - 1;
        for(int i=0; i<searchWord.length(); i++){
            vector<string> result;
            char c = searchWord[i];
            while(left <= right && (products[left].length() == i || products[left][i] < c)){
                left++;
            }
            while(left <= right && (products[right].length() == i || products[right][i] > c)){
                right--;
            }
            for(int j=0; j<3 && left+j<=right; j++){
                result.push_back(products[left+j]);
            }
            List.push_back(result);
        }
        return List;
    }
};