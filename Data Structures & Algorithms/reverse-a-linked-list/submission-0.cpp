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
        stack<ListNode*> sus;
        while(head != nullptr){
            sus.push(head);

            head = head->next;
        }

        if(sus.empty()) return nullptr;
        head = new ListNode(sus.top()->val);
        sus.pop();
        ListNode* rslt = head;
        while(!sus.empty()){
            head->next = sus.top();
            head = head->next;

            sus.pop();
        }

        head->next = nullptr;

        return rslt;
    }
};
