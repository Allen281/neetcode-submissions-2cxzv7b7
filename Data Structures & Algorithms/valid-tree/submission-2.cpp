class Solution {
public:
    vector<vector<int>> adj;
    vector<bool> visited;
    bool cycleFound = false;
    int nodes = 0;

    void dfs(int i, int prev){
        if(visited[i]){
            cycleFound = true;
            return;
        }

        visited[i] = true;
        nodes++;
        for(int a : adj[i]){
            if(a == prev) continue;

            dfs(a, i);
        }
        visited[i] = false;
    }

    bool validTree(int n, vector<vector<int>>& edges) {
        adj.resize(n);
        visited.resize(n);

        for(vector<int> e : edges){
            if(e[0] == e[1]) return false;

            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }

        dfs(0, 0);

        if(cycleFound || nodes != n) return false;

        return true;
    }
};
