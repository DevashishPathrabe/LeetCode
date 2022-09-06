class Solution {
    public String bestHand(int[] ranks, char[] suits) {
        int flag = -1;
        int arr[] = new int[5];
        int arr1[] = new int[14];
        for (int i=0; i<5; i++){
            arr[suits[i]-'a']++;
            arr1[ranks[i]]++;
        }
        for (int i=0; i<5; i++){
            if (arr[i] >= 5){
                return "Flush";
            }
        }
        for (int i=0; i<14; i++){
            if (arr1[i] >= 3){
                flag = 0;
                break;
            }
            if (arr1[i] == 2){
                flag = 1;
            }
        }
        if (flag == 0){
            return "Three of a Kind";
        }
        else if (flag == 1){
            return "Pair";
        }
        return "High Card";
    }
}