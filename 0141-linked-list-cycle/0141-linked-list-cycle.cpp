/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        unordered_set<ListNode*> mySet;
        bool cycle=false;
        ListNode* iterator=head;
        while(!cycle && iterator!= nullptr){
            if(mySet.count(iterator)) cycle=true;
            else mySet.insert(iterator);
            iterator=iterator->next;
        }
        return cycle;
    }
};