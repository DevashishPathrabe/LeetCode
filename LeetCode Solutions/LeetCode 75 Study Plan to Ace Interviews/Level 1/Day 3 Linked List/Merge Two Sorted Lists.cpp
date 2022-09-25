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
        ListNode *newNode = new ListNode(0);
        ListNode *requiredNode = newNode;
        while(list1 != NULL || list2 != NULL){
            if(list2 == NULL){
                requiredNode->next = list1;
                break;
            }
            if(list1 == NULL){
                requiredNode->next = list2;
                break;
            }
            if(list1->val > list2->val){
                requiredNode->next = new ListNode(list2->val);
                list2 = list2->next;
            } else{
                requiredNode->next = new ListNode(list1->val);
                list1 = list1->next;
            }
            requiredNode = requiredNode->next;
        }
        return newNode->next;
    }
};