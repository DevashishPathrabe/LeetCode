class Solution {
    public boolean carPooling(int[][] trips, int capacity) {
        int car[] = new int[1001];
		for (int i=0; i<trips.length; i++){
			car[trips[i][1]] += trips[i][0];
			car[trips[i][2]] -= trips[i][0];
		}
		int passengers = 0;
		for (int p: car){
			passengers += p;
			if (passengers > capacity){
				return false;
            }
		}
		return true;
    }
}