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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if(list1 == nullptr) return list2;
        if(list2 == nullptr) return list1;
        ListNode* res =new ListNode(min(list1->val,list2->val)-10);
        ListNode* current=res;
        ListNode* iterator1 = list1;
        ListNode* iterator2 = list2;
        while(iterator1 != nullptr || iterator2 != nullptr){
            if(iterator1 != nullptr && iterator2 != nullptr && iterator1->val <= iterator2->val){
                ListNode * newNode = iterator1;
                iterator1 = iterator1->next;
                newNode->next=nullptr;
                current->next=newNode;
                current=current->next;
            }else if(iterator1 != nullptr && iterator2 != nullptr && iterator1->val > iterator2->val){
                ListNode * newNode = iterator2;
                iterator2 = iterator2->next;
                newNode->next=nullptr;
                current->next=newNode;
                current=current->next;
            }else if( iterator2 != nullptr){
                ListNode * newNode = iterator2;
                iterator2 = iterator2->next;
                newNode->next=nullptr;
                current->next=newNode;
                current=current->next;
            }else if(iterator1 != nullptr ){
                ListNode * newNode = iterator1;
                iterator1 = iterator1->next;
                newNode->next=nullptr;
                current->next=newNode;
                current=current->next;
            }
        }

        return res->next;
    }
};