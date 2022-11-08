class Solution {
    public String removeDuplicates(String s, int k) {
        for(int i=1, count=1; i<s.length(); i++){
            count = s.charAt(i) == s.charAt(i-1) ? count + 1 : 1;
            if(count == k){
                s = removeDuplicates(s.substring(0, i-k+1) + s.substring(i+1), k);
            }
        }
        return s;
    }
}