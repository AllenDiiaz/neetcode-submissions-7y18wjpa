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
    void reorderList(ListNode* head) {

        // head → [1]→[2]→[3]→[4]→[5]→[6]→None
        
        // Mid pt
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast && fast->next)
        {
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode* second = slow->next;
        slow->next = nullptr;

        // Reverse
        ListNode* prev = nullptr;
        ListNode* cur = second;

        while (cur)
        {
            ListNode* temp = cur->next;
            cur->next = prev;
            prev = cur;
            cur = temp;
        }
        second = prev;

        // Cross Merge
        ListNode* first = head;
        ListNode* t1;
        ListNode* t2;

        while (second)
        {
            t1 = first->next;
            t2 = second->next;

            first->next = second;
            second->next = t1;

            first = t1;
            second = t2;
        }

        


        
        
    }
};
