class Solution {
public:
    vector<bool> visited;
    vector<vector<int>> adj;

    void dfs(int i){
        if(visited[i]) return;

        visited[i] = true;
        for(int n : adj[i]) dfs(n);
    }

    int countComponents(int n, vector<vector<int>>& edges) {
        visited.resize(n);
        adj.resize(n);

        for(vector<int> e : edges){
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }

        int counter = 0;
        for(int i = 0; i < n; i++){
            if(!visited[i]){
                counter++;
                dfs(i);
            }
        }

        return counter;
    }
};
