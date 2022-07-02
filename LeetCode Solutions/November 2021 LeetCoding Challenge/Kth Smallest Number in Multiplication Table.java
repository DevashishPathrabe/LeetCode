class Solution {
    public int count(int m, int n, int x) {
        int result = 0;
        for (int i=1; i<=m; i++){ 
            result += Math.min(x / i, n);
        }
        return result;
    }
    public int findKthNumber(int m, int n, int k) {
        int left = 1, right = m*n, mid, smallestNumber=0;
        while (left <= right){
            mid = (left + right) >> 1;
            if (count(m, n, mid) < k){
                left = mid + 1;
            } else{
                right = mid - 1;
                smallestNumber = mid;
            }
        }
        return smallestNumber;
    }
}