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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if(lists.size() == 0) return nullptr;
        if(lists.size() == 1) return lists[0];

        vector<ListNode*> merges;
        for(int i = 0; i < lists.size(); i += 2){
            if(i == lists.size()-1) merges.push_back(lists[i]);
            else merges.push_back(mergeLists(lists[i], lists[i+1]));
        }

        return mergeKLists(merges);
    }

    ListNode* mergeLists(ListNode* a, ListNode* b){
        ListNode* rslt = new ListNode();
        ListNode* head = rslt;

        while(a != nullptr && b != nullptr){
            if(a->val < b->val){
                rslt->next = a;
                a = a->next;
            } else{
                rslt->next = b;
                b = b->next;
            }

            rslt = rslt->next;
        }

        if(a != nullptr) rslt->next = a;
        else if(b != nullptr) rslt->next = b;
        else rslt->next = nullptr;

        return head->next;
    }
};
