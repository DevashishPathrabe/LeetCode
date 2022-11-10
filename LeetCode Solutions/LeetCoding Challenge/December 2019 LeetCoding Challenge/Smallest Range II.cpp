class Solution {
public:
    int smallestRangeII(vector<int>& A, int K) {
        if(A.size() == 1){
			return 0;
		}
		int difference = INT_MAX;
		int index = 0;
		vector<int> B;
		B = A;
		sort(B.begin(), B.end());
		for(int i=1; i<B.size(); i++){
			int maximum = max(B[i-1]+K, B.back()-K);
			int minimum = min(B[0]+K, B[i]-K);
			if(maximum-minimum < difference){
				difference = maximum-minimum;
				index = i;
			}
		}
		int a = INT_MAX;
		int b = INT_MIN;
		for(int i=0; i<A.size(); i++){
			if(A[i] > b){
				b = A[i];
			}
			if(A[i] < a){
				a = A[i];
			}
		}
		difference = min(difference, b-a);
		return difference;
    }
};