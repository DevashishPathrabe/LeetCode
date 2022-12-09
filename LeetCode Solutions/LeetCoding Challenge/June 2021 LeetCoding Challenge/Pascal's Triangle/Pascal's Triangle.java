class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> firstNumRows = new ArrayList<List<Integer>>(numRows);
        for (int i=0; i<numRows; i++){
            List<Integer> row = new ArrayList<>(i+1);
            while (row.size() <= i){
                row.add(1);
            }
            int mid = i >> 1;
            for (int j=1; j<=mid; j++){
                int val = firstNumRows.get(i-1).get(j-1) + firstNumRows.get(i-1).get(j);
                row.set(j, val);
                row.set(row.size()-j-1, val);
            }
            firstNumRows.add(row);
        }
        return firstNumRows;
    }
}