class MyHashMap {
private:
    struct Node{
        int key;
        int val;
        Node* next;
    };

    static inline int getHashIndex(int key){
        return key%1000;
    }

public:
    vector<Node*> buckets{1000, nullptr};
    MyHashMap() {}

    ~MyHashMap(){
        for(Node* node : buckets){
            while(node){
                Node* temp = node->next;
                delete node;
                node = temp;
            }
        }
    }
    
    void put(int key, int val) {
        int index = getHashIndex(key);
        Node* cur = buckets[index];
        while(cur){
            if(cur->key == key){
                cur->val = val;
                return;
            }
            cur = cur->next;
        }

        Node* newNode = new Node{key, val, buckets[index]};
        buckets[index] = newNode;
    }
    
    void remove(int key) {
        int index = getHashIndex(key);
        Node* curNode = buckets[index];
        Node* prev = nullptr;

        while(curNode){
            if(curNode->key == key){
                if(!prev) buckets[index] = curNode->next;
                else prev->next = curNode->next;
                delete curNode;
                return;
            }

            prev = curNode;
            curNode = curNode->next;
        }
    }
    
    int get(int key) {
        int index = getHashIndex(key);
        Node* curNode = buckets[index];

        while(curNode){
            if(curNode->key == key) return curNode->val;
            curNode = curNode->next;
        }

        return -1;
    }
};