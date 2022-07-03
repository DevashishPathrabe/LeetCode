

int maxScoreSightseeingPair(int* values, int valuesSize){
    int a = values[0], b = 0;
    for (int i=1; i<valuesSize; i++){
        b = fmax(a + values[i] - i, b);
        a = fmax(values[i] + i, a);
    }
    return b;
}