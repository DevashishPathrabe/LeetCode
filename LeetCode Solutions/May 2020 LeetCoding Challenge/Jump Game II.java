class Solution {
    public int jump(int[] nums) {
        int numsLength = nums.length - 1, current = -1, next = 0, result = 0;
        for(int i=0; next<numsLength; i++){
            if(i > current){
                result++;
                current = next;
            };
            next = Math.max(next, nums[i] + i);
        };
        return result;
    }
}