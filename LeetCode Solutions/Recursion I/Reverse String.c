

void reverseString(char* s, int sSize){
    char temp;
    for(int i=0, j=sSize-1; i<j; i++, j--){
        temp = s[j];
        s[j] = s[i];
        s[i] = temp;
    }
}