class LRUCache {
public:
    struct Node{
        Node* prev;
        Node* next;
        int val;
        int key;
    };

    Node* createNode(int val, int key){
        Node* cur = new Node;
        cur->prev = NULL;
        cur->next = NULL;
        cur->val = val;
        cur->key = key;

        return cur;
    }

    unordered_map<int, Node*> hm;
    int size, capacity;
    Node *mostRecent, *leastRecent;

    LRUCache(int capacity) {
        mostRecent = NULL;
        leastRecent = NULL;
        size = 0;
        this->capacity = capacity;
        hm.clear();
    }

    void bringToFront(Node* cur){
        if(cur == mostRecent) return;

        if(cur == leastRecent){
            cur->prev->next = NULL;
            leastRecent = cur->prev;
        } else if(cur->prev && cur->next){
            cur->prev->next = cur->next;
            cur->next->prev = cur->prev;
        }

        cur->next = mostRecent;
        mostRecent->prev = cur;
        cur->prev = NULL;
        mostRecent = cur;
    }

    void removeLRU(){
        if(!leastRecent) return;

        hm.erase(leastRecent->key);

        if(leastRecent->prev){
            leastRecent->prev->next = NULL;
            leastRecent = leastRecent->prev;
        } else{
            leastRecent = NULL;
            mostRecent = NULL;
        }
    }
    
    int get(int key) {
        if(!hm.contains(key)) return -1;

        Node* cur = hm[key];
        bringToFront(cur);

        return cur->val;
    }
    
    void put(int key, int value) {
        if(!hm.contains(key)){
            if(size == capacity){
                removeLRU();
                size--;
            }

            Node* newNode = createNode(value, key);

            if(!mostRecent && !leastRecent){
                mostRecent = newNode;
                leastRecent = newNode;
            } else bringToFront(newNode);  

            hm[key] = newNode;
            size++;
        } else{
            Node* node = hm[key];
            node->val = value;
            bringToFront(node);
        }
    }
};
