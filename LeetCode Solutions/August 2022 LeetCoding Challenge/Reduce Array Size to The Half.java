class Solution {
    public int minSetSize(int[] arr) {
        HashMap<Integer, Integer> count = new HashMap<>();
        for(int x : arr){
            count.put(x, count.getOrDefault(x, 0) + 1);
        }
        int[] frequencies = new int[count.values().size()];
        int i = 0;
        for(int freq : count.values()){
            frequencies[i++] = freq;
        }
        Arrays.sort(frequencies);
        int minimumSize = 0, removed = 0, half = arr.length / 2;
        i = frequencies.length - 1;
        while(removed < half){
            minimumSize += 1;
            removed += frequencies[i--];
        }
        return minimumSize;
    }
}