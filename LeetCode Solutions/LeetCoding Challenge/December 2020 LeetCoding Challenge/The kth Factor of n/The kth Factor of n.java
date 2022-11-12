class Solution {
    public int kthFactor(int n, int k) {
        int i = 1, count = 0;
        while (i <= n){
            if (n%i == 0){
                count++;
            }
            if (count == k){
                return i;
            }
            i++;
        }
        return -1;
    }
}