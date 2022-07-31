class Solution {
    public int heightChecker(int[] heights) {
        int[] array = new int[heights.length];
        for (int i=0; i<array.length; i++){
            array[i] = heights[i];
        }
        Arrays.sort(heights);
        int numberOfStudents = 0;
        for (int i=0; i<heights.length; i++){
            if (array[i] != heights[i]){
                numberOfStudents++;
            }
        }
        return numberOfStudents;
    }
}