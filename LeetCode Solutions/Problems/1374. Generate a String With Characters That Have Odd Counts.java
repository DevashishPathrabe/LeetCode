class Solution {
    public String generateTheString(int n) {
        char[] result = new char[n];
        int i = 0;
        while (i < n - 1){
            result[i] = 'a';
            i++;
        }
        if (n % 2 != 0){
            result[i] = 'a';
        }
        else{
            result[i] = 'b';
        }
        return new String(result);
    }
}