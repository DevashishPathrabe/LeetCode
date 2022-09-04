class Solution {
    public int[] sortedSquares(int[] A) {
        for (int number=0; number<A.length; number++){
            A[number] = A[number] * A[number];
        }
        Arrays.sort(A);
        return A;
    }
}