

bool validateStackSequences(int* pushed, int pushedSize, int* popped, int poppedSize){
    int lenP = pushedSize, i = 0, j = 0, sp = 0;
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