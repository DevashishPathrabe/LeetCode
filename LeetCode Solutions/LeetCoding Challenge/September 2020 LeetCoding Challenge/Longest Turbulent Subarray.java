class Solution {
    public int maxTurbulenceSize(int[] arr) {
        int increment = 1, decrement = 1, result = 1;
        for (int i=1; i<arr.length; i++){
            if (arr[i] < arr[i-1]){
                decrement = increment + 1;
                increment = 1;
            }
            else if (arr[i] > arr[i-1]){
                increment = decrement + 1;
                decrement = 1;
            }
            else{
                increment = 1;
                decrement = 1;
            }
            result = Math.max(result, Math.max(increment, decrement));
        }
        return result;
    }
}