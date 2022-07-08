class Solution {
public:
    int countEven(int num) {
        int sum = 0, n = num;
        for (sum = 0; num > 0; sum += num % 10, num /= 10);
        return (sum & 1) ? (n - 1) / 2: n / 2;
    }
};