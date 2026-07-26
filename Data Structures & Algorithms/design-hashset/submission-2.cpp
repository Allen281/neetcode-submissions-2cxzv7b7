class MyHashSet {
private:
    struct Node{
        int val;
        Node* next;
    };

    static inline int getHashIndex(int key){
        return key%1000;
    }

public:
    vector<Node*> buckets{1000, nullptr};
    MyHashSet() {}

    ~MyHashSet(){
        for(Node* node : buckets){
            while(node){
                Node* temp = node->next;
                delete node;
                node = temp;
            }
        }
    }
    
    void add(int key) {
        if(contains(key)) return;

        int index = getHashIndex(key);
        Node* newNode = new Node{key, buckets[index]};
        buckets[index] = newNode;
    }
    
    void remove(int key) {
        int index = getHashIndex(key);
        Node* curNode = buckets[index];
        Node* prev = nullptr;

        while(curNode){
            if(curNode->val == key){
                if(!prev) buckets[index] = curNode->next;
                else prev->next = curNode->next;
                delete curNode;
                return;
            }

            prev = curNode;
            curNode = curNode->next;
        }
    }
    
    bool contains(int key) {
        int index = getHashIndex(key);
        Node* curNode = buckets[index];

        while(curNode){
            if(curNode->val == key) return true;
            curNode = curNode->next;
        }

        return false;
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */