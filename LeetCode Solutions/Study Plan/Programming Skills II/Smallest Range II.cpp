class Solution {
public:
    int smallestRangeII(vector<int>& nums, int k) {
        if(nums.size() == 1){
			return 0;
		}
		int difference = INT_MAX;
		int index = 0;
		vector<int> B;
		B = nums;
		sort(B.begin(), B.end());
		for(int i=1; i<B.size(); i++){
			int maximum = max(B[i-1]+k, B.back()-k);
			int minimum = min(B[0]+k, B[i]-k);
			if(maximum-minimum < difference){
				difference = maximum-minimum;
				index = i;
			}
		}
		int a = INT_MAX;
		int b = INT_MIN;
		for(int i=0; i<nums.size(); i++){
			if(nums[i] > b){
				b = nums[i];
			}
			if(nums[i] < a){
				a = nums[i];
			}
		}
		difference = min(difference, b-a);
		return difference;
    }
};