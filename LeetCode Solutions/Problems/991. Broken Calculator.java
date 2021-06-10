class Solution {
    public int brokenCalc(int x, int y) {
        int result = 0;
        while(x < y){
            result++;
            if(y % 2 > 0){
                y++;
            } else{
                y /= 2;
            }
        }
        return result + x - y;
    }
}