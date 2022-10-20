class Solution {
    final static int[] value = {1000,900,500,400,100,90,50,40,10,9,5,4,1};
    final static String[] symbol = {"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
    public String intToRoman(int num) {
        StringBuilder romanNumeral = new StringBuilder();
        for (int i=0; num>0; i++){
            while (num >= value[i]){
                romanNumeral.append(symbol[i]);
                num -= value[i];
            }
        }
        return romanNumeral.toString();
    }
}