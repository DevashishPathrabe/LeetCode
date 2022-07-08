class Solution {
public:
    long long maximumSubsequenceCount(string text, string pattern) {
        long long result = 0, count1 = 0, count2 = 0;
        for (char& c: text) {
            if (c == pattern[1])
                result += count1, count2++;
            if (c == pattern[0])
                count1++;
        }
        return result + max(count1, count2);
    }
};