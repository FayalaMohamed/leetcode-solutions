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
        ListNode* nouvListe = nullptr;
        ListNode* iterator =head ;
        int nb=0;
        while(iterator != nullptr){
            ListNode * nouvElem = new ListNode(iterator->val,nouvListe);
            nouvListe=nouvElem ;
            iterator=iterator->next;
        }
        return nouvListe;
         
    }
};