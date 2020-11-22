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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode *newNode = new ListNode(0);
        ListNode *requiredNode = newNode;
        while(l1 != NULL || l2 != NULL){
            if(l2 == NULL){
                requiredNode->next = l1;
                break;
            }
            if(l1 == NULL){
                requiredNode->next = l2;
                break;
            }
            if(l1->val > l2->val){
                requiredNode->next = new ListNode(l2->val);
                l2 = l2->next;
            } else{
                requiredNode->next = new ListNode(l1->val);
                l1 = l1->next;
            }
            requiredNode = requiredNode->next;
        }
        return newNode->next;
    }
};