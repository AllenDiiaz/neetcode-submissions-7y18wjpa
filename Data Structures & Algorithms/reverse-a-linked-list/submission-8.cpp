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
    ListNode* reverseList(ListNode* head) {

        ListNode* prev = nullptr;
        ListNode* cur = head;

        while (cur)
        {
            // 記住下一個 ptr
            ListNode* temp = cur->next;
            // 反轉 ptr
            cur->next = prev;
            // 更新 prev
            prev = cur;
            // 更新 curr
            cur = temp;
        }

        return prev;
        
    }
};
