class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        parent.resize(edges.size()+1);
        for(int i=0; i<parent.size(); i++){
            parent[i] = i;
        }
        for(auto& e : edges){
            if(find(e[0]) == find(e[1])){
                return e;
            }
            else{
                uniun(e[0], e[1]);
            }
        }
        return edges[0];
    }
private:
    vector<int> parent;
    int find(int x){
        if(x != parent[x]) parent[x] = find(parent[x]);
        return parent[x];
    }
    void uniun(int x, int y){
        parent[find(y)] = find(x);
    }
};