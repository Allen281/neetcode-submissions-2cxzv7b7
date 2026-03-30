class Solution {
public:
    string goal;
    vector<vector<bool>> visited;
    bool exist(vector<vector<char>>& board, string word) {
        goal = word;

        for(int r = 0; r < board.size(); r++){
            for(int c = 0; c < board[r].size(); c++){
                if(board[r][c] == word[0]){
                    visited.clear();
                    visited.resize(board.size(), vector<bool>(board[0].size()));   
                    if(dfs(board, r, c, 0)) return true;
                }
            }
        }
        
        return false;
    }

    bool dfs(vector<vector<char>>& board, int r, int c, int wordI){
        if(wordI == goal.size()) return true;
        if(r < 0 || r >= board.size() || c < 0 || c >= board[r].size()) return false;
        if(visited[r][c]) return false;
        if(board[r][c] != goal[wordI]) return false;

        visited[r][c] = true;
        if(dfs(board, r+1, c, wordI+1)) return true;
        if(dfs(board, r-1, c, wordI+1)) return true;
        if(dfs(board, r, c+1, wordI+1)) return true;
        if(dfs(board, r, c-1, wordI+1)) return true;
        visited[r][c] = false;

        return false;
    }
};
