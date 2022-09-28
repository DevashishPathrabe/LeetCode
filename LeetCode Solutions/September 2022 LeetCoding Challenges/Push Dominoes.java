class Solution {
    public String pushDominoes(String dominoes) {
        int n = dominoes.length();
        char[] chars = dominoes.toCharArray();
        int leftI = 0, rightI = 1;
        while (rightI < n){
            while (rightI < n && chars[rightI] == '.')
                rightI++;
            if (rightI == n){
                break;
            }
            if (chars[leftI] == '.' && chars[rightI] == 'L'){
                while (leftI != rightI){
                    chars[leftI++] = 'L';
                }
                rightI++;
            }
            else if (chars[leftI] == 'L' && chars[rightI] == 'R'){
                leftI = rightI;
                rightI = rightI + 1;
            }
            else if (chars[leftI] == 'R' && chars[rightI] == 'L'){
                int tempRightI = rightI;
                while (leftI < tempRightI){
                    chars[leftI] = 'R';
                    chars[tempRightI] = 'L';
                    leftI++;tempRightI--;
                }
                leftI = rightI;
                rightI++;
            }
            else if (chars[leftI] == 'R'){
                while (leftI != rightI){
                    chars[leftI++] = 'R';
                }
                rightI++;
            }
            else if (chars[rightI] == 'L' && chars[leftI] == 'L'){
                while (leftI != rightI){
                    chars[leftI++] = 'L';
                }
                rightI++;
            }
            else if (chars[rightI] == 'R' && chars[leftI] == '.'){
                leftI = rightI;
                rightI++;
            }
        }
        if (leftI < n-1 && chars[leftI] == 'R'){
            while (leftI < n){
                    chars[leftI++] = 'R';
            }
        }
        return new String(chars);
    }
}