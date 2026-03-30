class Solution {
private:
    int R, C;
    // Use boolean vectors for clarity, initialized to false
    vector<vector<bool>> pacific; 
    vector<vector<bool>> atlantic; 
    vector<vector<int>> grid; // Store heights

    void dfs(int r, int c, int prevHeight, vector<vector<bool>>& reachable) {
        // 1. Bounds Check
        if (r < 0 || r >= R || c < 0 || c >= C) return;
        
        // 2. Visited Check (Base Case: Already marked as reachable)
        if (reachable[r][c]) return;

        // 3. Height Check (Reverse Flow: must move to equal or higher ground)
        if (grid[r][c] < prevHeight) return;

        // Mark the current cell as reachable
        reachable[r][c] = true; 

        // Recursive Calls (Move to the neighbors)
        dfs(r + 1, c, grid[r][c], reachable);
        dfs(r - 1, c, grid[r][c], reachable);
        dfs(r, c + 1, grid[r][c], reachable);
        dfs(r, c - 1, grid[r][c], reachable);
    }

public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        if (heights.empty()) return {};
        R = heights.size();
        C = heights[0].size();
        grid = heights;

        // Initialize reachability matrices to false
        pacific.assign(R, vector<bool>(C, false));
        atlantic.assign(R, vector<bool>(C, false));
        
        // Run DFS from all Pacific borders (top row, left column)
        for (int c = 0; c < C; ++c) dfs(0, c, INT_MIN, pacific); // Top row
        for (int r = 0; r < R; ++r) dfs(r, 0, INT_MIN, pacific); // Left column

        // Run DFS from all Atlantic borders (bottom row, right column)
        for (int c = 0; c < C; ++c) dfs(R - 1, c, INT_MIN, atlantic); // Bottom row
        for (int r = 0; r < R; ++r) dfs(r, C - 1, INT_MIN, atlantic); // Right column
        
        vector<vector<int>> result;
        // Find cells reachable by both
        for (int r = 0; r < R; ++r) {
            for (int c = 0; c < C; ++c) {
                if (pacific[r][c] && atlantic[r][c]) {
                    result.push_back({r, c});
                }
            }
        }
        return result;
    }
};