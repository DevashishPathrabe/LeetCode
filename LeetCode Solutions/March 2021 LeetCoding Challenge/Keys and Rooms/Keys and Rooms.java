class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        boolean[] arr = new boolean[rooms.size()];
        arr[0] = true;
        Stack<Integer> stack = new Stack<>();
        stack.push(0);
        int count = 1;
        while (stack.size() > 0){
            for (int k : rooms.get(stack.pop())){
                if (!arr[k]){
                    stack.push(k);
                    arr[k] = true;
                    count++;
                }
            }
        }
        return rooms.size() == count;
    }
}