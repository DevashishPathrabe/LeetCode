class Solution {
    public List<Integer> maxScoreIndices(int[] nums) {
        int currentScore = Arrays.stream(nums).sum();
        int currentMax = currentScore;
        List<Integer> result = new ArrayList<>();
        result.add(0);
        for (int i=1; i<=nums.length; ++i){
            currentScore += 1 - 2 * nums[i - 1];
            if (currentScore > currentMax) {
                currentMax = currentScore;
                result.clear();
                result.add(i);
            } 
            else if (currentScore == currentMax){
                result.add(i);
            }
        }
        return result;
    }
}