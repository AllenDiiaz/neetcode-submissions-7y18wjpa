/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {

        ListNode  vir(0,head);
        ListNode* left = &vir;

        while (true) {
            
            ListNode* last = getKth(left,k);
            if (!last) break;
            ListNode* right = last->next;

            ListNode* prev = right;
            ListNode* cur = left->next;
            while (cur != right)
                {
                    ListNode* tmp = cur->next;
                    cur->next = prev;
                    prev = cur;
                    cur = tmp;
                }

            ListNode* first = left->next;
            left->next = last;
            left = first;            
        }

        return vir.next;      
    }
private:
    ListNode* getKth(ListNode* cur, int k)
    {
        while (cur && k > 0)
            {
                cur = cur->next;
                k--;
            }
        return cur;
    }
};
