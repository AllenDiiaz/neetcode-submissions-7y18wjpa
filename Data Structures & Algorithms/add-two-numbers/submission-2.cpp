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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {

        ListNode vir;
        ListNode* cur = &vir;
        int carry = 0;

        while (l1 || l2 || carry)
        {
            int v1 = l1 ? l1->val : 0;
            int v2 = l2 ? l2->val : 0;

            int total = carry + v1 + v2;
            carry = total / 10;
            int digit = total % 10;

            cur->next = new ListNode(digit);
            cur = cur->next;

            l1 = l1 ? l1->next : nullptr;
            l2 = l2 ? l2->next : nullptr;
        }

        return vir.next;
        
    }
};
