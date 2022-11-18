class Solution {
public:
    int partitionDisjoint(vector<int>& nums) {
        int max = nums[0];
        for(int i=0; i<nums.size()-1; i++){
            int flag=1;
            if(nums[i] > max){
                max = nums[i];
            }
            for(int j=i+1; j<nums.size(); j++){
                if(nums[j] < max){
                    flag = 0;
                    break;
                }
            }
            if(flag == 1){
                return i+1;
            }
        }
        return 0;
    }
};