/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2){
    struct ListNode *newNode = void ListNode(0);
    struct ListNode *requiredNode = newNode;
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
            requiredNode->next = void ListNode(l2->val);
            l2 = l2->next;
        } else{
            requiredNode->next = void ListNode(l1->val);
            l1 = l1->next;
        }
        requiredNode = requiredNode->next;
    }
    return newNode->next;
}