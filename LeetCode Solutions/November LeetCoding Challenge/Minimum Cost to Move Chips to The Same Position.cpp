class Solution {
public:
    int minCostToMoveChips(vector<int>& position) {
        int oddNumbers = 0;
        int evenNumbers = 0;
        for(int i : position){
            if(i%2 == 0){
                evenNumbers += 1;
            } else{
                oddNumbers += 1;
            }
        }
        if(evenNumbers > oddNumbers){
            return oddNumbers;
        }
        return evenNumbers;
    }
};