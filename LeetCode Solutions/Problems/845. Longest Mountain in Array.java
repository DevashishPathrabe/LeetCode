class Solution {
    public int longestMountain(int[] arr) {
        int left = 0;
        int right = 1;
        int length = 0;
        while(right < arr.length){
            if(arr[left] >= arr[right]){
                left += 1;
                right += 1;
            } else{
                int haveRight = 0;
                while(right < (arr.length-1) && arr[right] < arr[right+1]){
                    right += 1;
                }
                while(right < (arr.length-1) && arr[right] > arr[right+1]){
                    right += 1;
                    haveRight = 1;
                }
                if(haveRight != 0){
                    length = Math.max(length,right-left+1);
                }
                left = right;
                right = left + 1;
            }
        }
        return length;
    }
}