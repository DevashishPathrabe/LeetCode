class Solution {
    int result;
    public int longestPath(int[] parent, String s) {
        result = 0;
        ArrayList<Integer>[] children = new ArrayList[parent.length];
        for (int i=0; i<parent.length; i++){
            children[i] = new ArrayList<>();
        }
        for (int i=1; i<parent.length; i++){
            children[parent[i]].add(i);
        }
        helper(children, s, 0);
        return result;
    }

    private int helper(ArrayList<Integer>[] children, String s, int i) {
        PriorityQueue<Integer> queue = new PriorityQueue<>();
        for (int j : children[i]){
            int current = helper(children, s, j);
            if (s.charAt(j) != s.charAt(i)){
                queue.offer(-current);
            }
        }
        int big1 = queue.isEmpty() ? 0 : -queue.poll();
        int big2 = queue.isEmpty() ? 0 : -queue.poll();
        result = Math.max(result, big1 + big2 + 1);
        return big1 + 1;
    }
}