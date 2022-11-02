bool isPalindrome(int x){
    long reverseNumber = 0;
    int temp = x;
    while (x > 0){
        int remainder = x % 10;
        reverseNumber = reverseNumber * 10 + remainder;
        x /= 10;
    }
    if (temp == reverseNumber){
        return true;
    }
    else{
        return false;
    }
}