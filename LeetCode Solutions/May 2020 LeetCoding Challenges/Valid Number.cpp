class Solution {
public:
    bool isNumber(string s) {
        bool num = false, exponent = false, sign = false, decimal = false;
        for(auto c : s)
            if(c >= '0' && c <= '9'){
                num = true;
            }
            else if(c == 'e' || c == 'E'){
                if(exponent || !num){
                    return false;
                }
                else{
                    exponent = true, sign = false, num = false, decimal = false;
                }
            }
            else if(c == '+' || c == '-'){
                if(sign || num || decimal){
                    return false;
                }
                else{
                    sign = true;
                }
            }
            else if(c == '.'){
                if(decimal || exponent){
                    return false;
                }
                else{
                    decimal = true;
                }
            }
            else{
                return false;
            }
        return num;
    }
};