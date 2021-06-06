class Solution {
public:
    int heightChecker(vector<int>& heights) {
        int array = sort(heights.begin(),heights.end());
        int numberOfStudents = 0;
        for(int i=0; i<heights.length; i++){
            if(array[i] != heights[i]){
                numberOfStudents++;
            }
        }
        return numberOfStudents;
    }
};