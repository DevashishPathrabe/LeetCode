class Solution {
public:
    vector<int> advantageCount(vector<int>& nums1, vector<int>& nums2) {
        vector<int> order = vector<int>(nums2.size()), permutation = vector<int>(nums1.size());
        for(int i=0; i<nums2.size(); i++){
            order[i] = i;
        }
        sort(order.begin(), order.end(), [&](int a, int b) {return nums2[a] > nums2[b];});
        sort(nums1.begin(), nums1.end(), greater<>());
        int i = 0, j = nums2.size()-1;
        for(int ix : order){
            permutation[ix] = nums1[i] > nums2[ix] ? nums1[i++] : nums1[j--];
        }
        return permutation;
    }
};