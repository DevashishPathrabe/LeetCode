class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        vector<bool> arr(rooms.size(), false);
        arr[0] = true;
        stack<int> s = stack<int>({0});
        int count = 1;
        while (s.size()){
            vector<int> keys = rooms[s.top()];
            s.pop();
            for (int k : keys){
                if (!arr[k]){
                    s.push(k), arr[k] = true, count++;
                }
            }
        }
        return rooms.size() == count;
    }
};