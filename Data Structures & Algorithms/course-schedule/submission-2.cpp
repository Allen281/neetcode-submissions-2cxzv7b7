class Solution {
public:
    vector<vector<int>> adj;
    vector<bool> visited;
    bool cycleFound = false;

    void dfs(int i){
        if(visited[i]){
            cycleFound = true;
            return;
        }

        visited[i] = true;

        for(int n : adj[i]){
            dfs(n);
        }

        visited[i] = false;
    }

    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        adj.resize(numCourses);
        visited.resize(numCourses);

        for(vector<int> v : prerequisites){
            adj[v[0]].push_back(v[1]);
        }

        for(int i = 0; i < numCourses; i++){
            fill(visited.begin(), visited.end(), false);
            dfs(i);
            
            if(cycleFound) return false;
        }

        return true;
    }
};
