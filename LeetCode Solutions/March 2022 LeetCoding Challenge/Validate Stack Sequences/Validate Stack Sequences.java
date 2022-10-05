class Solution {
    public boolean validateStackSequences(int[] pushed, int[] popped) {
        int lenP = pushed.length, i = 0, j = 0, sp = 0;
        while(i < lenP){
            if(sp >= 0 && popped[j] == pushed[sp]){ 
                j++;
                sp--;
            } else{
                sp++;
                i++;
                if(i < lenP){
                    pushed[sp] = pushed[i];
                }
            }
        }
        return sp == 0;
    }
}