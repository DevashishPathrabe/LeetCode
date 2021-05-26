

int maxProfit(int* prices, int pricesSize, int fee){
    int buying = 0, selling = -prices[0];
    for(int i=1; i<pricesSize; i++){
        buying = fmax(buying, selling + prices[i] - fee);
        selling = fmax(selling, buying - prices[i]);
    }
    return buying;
}