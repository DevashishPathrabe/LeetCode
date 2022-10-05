class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        int lenP = pushed.size(), i = 0, j = 0, sp = 0;
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
};