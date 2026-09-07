class LRUCache {
private:
    struct Node {
    int key , val;
    Node* prev;
    Node* next;
    Node(int k, int v) : key(k), val(v), prev(nullptr), next(nullptr) {}
    };

    int cap;
    unordered_map<int, Node*> cache;
    Node* left;
    Node* right;

    void remove(Node* node) {
        node->prev->next = node->next;
        node->next->prev = node->prev;
    }

    void insertAtNew(Node* node) {
        Node* prev = right->prev;

        node->prev = prev;
        prev->next = node;

        node->next = right;
        right->prev = node;
    }

public:
    LRUCache(int capacity) {
        cap = capacity;
        left = new Node(0,0);
        right = new Node(0,0);

        left->next = right;
        right->prev = left;
    }
    
    int get(int key) {
        
        if (cache.find(key) == cache.end()) return -1;

        Node* node = cache[key];
        remove(node);
        insertAtNew(node);
        return node->val;
    }
    
    void put(int key, int value) {

        if (cache.count(key))
        {
            Node* old = cache[key];
            remove(old);
            delete old;
        }

        Node* node = new Node(key, value);
        cache[key] = node;
        insertAtNew(node);

        if ((int)cache.size() > cap)
        {
            Node* lru = left->next;
            remove(lru);
            cache.erase(lru->key);
            delete lru;
        }
        
    }
};
