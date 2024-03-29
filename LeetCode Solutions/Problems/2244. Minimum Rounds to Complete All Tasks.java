class Solution {
    public int minimumRounds(int[] tasks) {
        HashMap<Integer, Integer> count = new HashMap<>();
        for (int a : tasks)
            count.put(a, count.getOrDefault(a, 0) + 1);
        int result = 0;
        for (int freq : count.values()){
            if (freq == 1){
                return -1;
            }
            result += (freq + 2) / 3;
        }
        return result;
    }
}