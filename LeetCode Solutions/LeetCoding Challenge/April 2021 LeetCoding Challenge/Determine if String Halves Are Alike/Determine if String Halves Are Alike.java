class Solution {
    String vowels = "AEIOUaeiou";
    public boolean halvesAreAlike(String s) {
        int middle = s.length() / 2, result = 0;
        for (int i=0, j=middle; i<middle; i++, j++){
            if (vowels.indexOf(s.charAt(i)) >= 0){
                result++;
            }
            if (vowels.indexOf(s.charAt(j)) >= 0){
                result--;
            }
        }
        return result == 0;
    }
}