int hammingWeight(uint32_t n) {
    int numberOf1bits = 0;
    while (n != 0) {
        numberOf1bits += n%2;
        n = n>>1;
    }
    return numberOf1bits;
}