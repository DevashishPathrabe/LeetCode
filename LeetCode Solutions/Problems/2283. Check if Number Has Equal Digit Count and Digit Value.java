class Solution {
    public boolean digitCount(String num) {
        final int totalDigits = 10;
        int[] frequency = new int[totalDigits];
        for (int i=0; i<num.length(); ++i){
            frequency[num.charAt(i) - '0']++;
        }
        for (int i=0; i<num.length(); ++i){
            if (frequency[i] != (num.charAt(i) - '0')){
                return false;
            }
        }
        return true;
    }
}