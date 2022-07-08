class Solution {
    public int minMoves(int target, int maxDoubles) {
        int moves = 0;
        while(target > 1) {
            if(target % 2 == 0 && maxDoubles > 0)  {
                target /= 2;
                maxDoubles--;
            }
            else if(target % 2 == 1) {
                target--;
            } else{
                moves += (target - 1);
                target = 0;
                break;
            }
            moves++;
        }
        return moves;
    }
}