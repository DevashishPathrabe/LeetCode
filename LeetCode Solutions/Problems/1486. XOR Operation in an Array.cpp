class Solution {
public:
    int xorOperation(int n, int start) {
        int current = start;
        for(int i=1; i<n; i++){
            current = current ^ (start + (i * 2));
        }
        return current;
    }
};