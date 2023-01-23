class Solution {
    public int[] answerQueries(int[] nums, int[] queries) {
        Arrays.sort(nums);
        int n = nums.length, m = queries.length, result[] = new int[m];
        for (int i=1; i<n; ++i){
            nums[i] += nums[i - 1];
        }
        for (int i=0; i<m; ++i){
            int j = Arrays.binarySearch(nums, queries[i]);
            result[i] = Math.abs(j + 1);
        }
        return result;
    }
}