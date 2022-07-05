class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int max = -1, temp;
        for(int i=arr.size()-1; i>=0; i--){
            temp = arr[i];
            arr[i] = max;
            if(temp > max){
                max = temp;
            }
        }
        return arr;
    }
};