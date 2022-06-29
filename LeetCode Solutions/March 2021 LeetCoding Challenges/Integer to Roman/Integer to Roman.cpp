class Solution {
public:
    const int value[13] = {1000,900,500,400,100,90,50,40,10,9,5,4,1};
    const string symbol[13] = {"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
    string intToRoman(int num) {
        string romanNumeral = "";
        for (int i=0; num>0; i++){
            while (num >= value[i]){
                romanNumeral += symbol[i], num -= value[i];
            }
        }
        return romanNumeral;
    }
};