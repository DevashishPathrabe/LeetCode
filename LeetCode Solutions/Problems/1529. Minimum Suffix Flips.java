class Solution {
    public int minFlips(String target) {
        int flips = 0;
        for (char bit: target.toCharArray()){
            if ((bit - '0') - flips%2 != 0){
                flips += 1;
            }
        }
        return flips;
    }
}