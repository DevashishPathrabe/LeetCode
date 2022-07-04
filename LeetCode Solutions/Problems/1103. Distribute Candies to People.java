class Solution {
public:
    vector<int> distributeCandies(int candies, int num_people) {
        int j = 1;
        vector<int>v(num_people);
        int i = 0;
        while (candies > 0){
            if (j > candies){
                j = candies;
            }
            if (i == num_people){
                i = 0;
            }
            v[i] += j;
            candies -= j;
            j++;
            i++;
        }
        return v;
    }
};