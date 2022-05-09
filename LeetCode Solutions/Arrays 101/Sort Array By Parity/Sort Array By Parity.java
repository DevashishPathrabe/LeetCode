class Solution {
    public int[] sortArrayByParity(int[] A) {
        int left = 0;
        int right = A.length - 1;
        while (left < right){
            if (A[left] % 2 == 1){
                int temp = A[left];
                A[left] = A[right];
                A[right] = temp;
                right -= 1;
            } else{
                left += 1;
            }
        }
        return A;
    }
}