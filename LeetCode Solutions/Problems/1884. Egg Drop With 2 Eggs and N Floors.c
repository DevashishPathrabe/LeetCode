

int twoEggDrop(int n){
    int minimumNumberOfMoves = 0;
    int iterable = n;
    while (iterable > 0){
        minimumNumberOfMoves += 1;
        iterable -= minimumNumberOfMoves;
    }
    return minimumNumberOfMoves;
}