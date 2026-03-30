class WordDictionary {
public:
    struct Node{
        vector<Node*> children;
        char val;
        bool isWord;

        Node(char c, bool w){
            children.resize(26);
            val = c;
            isWord = w;
        }
    };

    Node* root;

    WordDictionary() {
        root = new Node('\0', false);
    }
    
    void addWord(string word) {
        Node* cur = root;
        for(char c : word){
            if(cur->children[c-'a'] == nullptr){
                cur->children[c-'a'] = new Node(c, false);
            }
            cur = cur->children[c-'a'];
        }

        cur->isWord = true;
    }
    
    bool search(string word) {
        return dfs(word, 0, root);
    }

    bool dfs(string word, int index, Node* cur) {
        if(cur == nullptr) return false;
        if(index >= word.size()) return cur->isWord;
        
        if(word[index] == '.'){
            for(Node* n : cur->children){
                if(dfs(word, index+1, n)) return true;
            }

            return false;
        }

        return dfs(word, index+1, cur->children[word[index]-'a']);
    }
};
