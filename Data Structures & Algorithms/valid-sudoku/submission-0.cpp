class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<vector<bool>> inRow(9, vector<bool>(9));
        vector<vector<bool>> inCol(9, vector<bool>(9));
        vector<vector<vector<bool>>> inSquare(9, vector<vector<bool>>(9, vector<bool>(9)));

        for(int r = 0; r < 9; r++){
            for(int c = 0; c < 9; c++){
                if(board[r][c] == '.') continue;

                int n = board[r][c]-'1';

                if(inRow[r][n]) return false;
                if(inCol[c][n]) return false;
                if(inSquare[r/3][c/3][n]) return false;

                inRow[r][n] = true;
                inCol[c][n] = true;
                inSquare[r/3][c/3][n] = true;
            }
        }

        return true;
    }
};
