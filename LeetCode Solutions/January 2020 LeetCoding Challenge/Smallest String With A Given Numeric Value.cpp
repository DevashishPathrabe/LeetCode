class Solution {
public:
    string getSmallestString(int n, int k) {
        k -= n;
        string numericValue = "_bcdefghijklmnopqrstuvwxy_";
        string lexicographicallySmallestString = std::string(~~(k / 25), 'z');
        if(k % 25){
            lexicographicallySmallestString = numericValue[k % 25] + lexicographicallySmallestString;
        }
        return std::string(n - lexicographicallySmallestString.size(), 'a') + lexicographicallySmallestString;
    }
};