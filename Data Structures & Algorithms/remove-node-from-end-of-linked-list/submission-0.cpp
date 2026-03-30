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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        n = getSize(head)-n+1;

        ListNode* prev = new ListNode();
        ListNode* rslt = prev;
        ListNode* cur = head;

        int counter = 1;
        while(counter < n){
            counter++;
            prev->next = cur;
            prev = prev->next;
            cur = cur->next;
        }

        prev->next = cur->next;

        return rslt->next;
    }

    int getSize(ListNode* head){
        int counter = 0;

        while(head != nullptr){
            counter++;
            head = head->next;
        }

        return counter;
    }
};
