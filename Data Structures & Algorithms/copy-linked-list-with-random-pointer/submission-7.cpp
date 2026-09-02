/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {

        unordered_map< Node*,Node* > oldToNew;

        Node* cur = head;
        while (cur)
        {
            oldToNew[cur] = new Node(cur->val);
            cur = cur->next;
        }

        cur = head;
        while (cur)
        {
            Node* copy = oldToNew[cur];
            copy->next = oldToNew[cur->next];
            copy->random = oldToNew[cur->random];
            cur = cur->next;
        }

        return oldToNew[head];




        
    }
};
