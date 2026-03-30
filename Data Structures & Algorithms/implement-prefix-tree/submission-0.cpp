class PrefixTree {
public:
    struct Node {
        char val;
        unordered_map<char, Node*> children;
        bool isWord;

        Node(char c){
            val = c;
            isWord = false;
        }
    };
    Node* root;

    PrefixTree() {
        root = new Node('\0');
    }
    
    void insert(string word) {
        Node* cur = root;
        for(int i = 0; i < word.size(); i++){
            if(cur->children[word[i]] == nullptr){
                cur->children[word[i]] = new Node(word[i]);
            }
            cur = cur->children[word[i]];
        }
        cur->isWord = true;
    }
    
    bool search(string word) {
        Node* cur = root;

        for(char c : word){
            if(cur->children[c] == nullptr) return false;
            cur = cur->children[c];
        }

        return cur->isWord;
    }
    
    bool startsWith(string prefix) {
        Node* cur = root;

        for(char c : prefix){
            if(cur->children[c] == nullptr) return false;
            cur = cur->children[c];
        }

        return true;
    }
};

