class Solution {
public:
    struct Node{
        vector<Node*> children;
        bool isWord;

        Node(){
            children.resize(26);
            isWord = false;
        }
    };

    Node* root;
    unordered_set<string> rslt;

    void addWord(string s){
        Node* cur = root;

        for(char c : s){
            if(cur->children[c-'a'] == nullptr) cur->children[c-'a'] = new Node();
            cur = cur->children[c-'a'];
        }

        cur->isWord = true;
    }

    void dfs(int r, int c, vector<vector<char>>& board, Node* node, string word){
        if(r < 0 || r >= board.size() || c < 0 || c >= board[r].size()) return;
        if(board[r][c] == '#' || node == nullptr) return;
        
        if(node->children[board[r][c]-'a'] == nullptr) return;
        
        word += board[r][c];
        node = node->children[board[r][c]-'a'];
        if(node->isWord) rslt.insert(word);

        board[r][c] = '#';

        dfs(r+1, c, board, node, word);
        dfs(r-1, c, board, node, word);
        dfs(r, c+1, board, node, word);
        dfs(r, c-1, board, node, word);

        board[r][c] = word[word.size()-1];
        word.erase(word.end()-1);
    }

    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        root = new Node();

        for(string w : words) addWord(w);

        string wordBuilder = "";
        for(int r = 0; r < board.size(); r++){
            for(int c = 0; c < board[r].size(); c++){
                dfs(r, c, board, root, wordBuilder);
            }
        }

        return vector<string>(rslt.begin(), rslt.end());
    }
};
