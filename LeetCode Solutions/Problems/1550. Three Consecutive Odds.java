class Solution {
    public boolean threeConsecutiveOdds(int[] arr) {
        if(arr.length < 3){
            return false;
        }
        for(int i=0; i<arr.length-2; i++){
            int odd1 = arr[i], odd2 = arr[i+1], odd3 = arr[i+2];
            if((odd1%2 !=0) && (odd2%2 !=0) && (odd3%2 !=0)){
                return true;
            }
        }
        return false;
    }
}