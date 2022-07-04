class Solution {
    public String[] findOcurrences(String text, String first, String second) {
        String[] s = text.split(" ");
        List<String> arr = new ArrayList<String>();
        for (int i=2; i<s.length; ++i){
            if (s[i-2].equals(first) && s[i-1].equals(second)){
                arr.add(s[i]);
            }
        }
        return arr.toArray(new String[0]);
    }
}