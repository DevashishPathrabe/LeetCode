class Solution {
    public void reverseString(char[] s) {
        char temp;
        for (int i=0, j=s.length-1; i<j; i++, j--){
            temp = s[j];
            s[j] = s[i];
            s[i] = temp;
        }
    }
}