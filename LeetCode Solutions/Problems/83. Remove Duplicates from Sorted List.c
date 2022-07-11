/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* deleteDuplicates(struct ListNode* head){
    if(head == NULL){
        return head;
    }
    struct ListNode* temp = head->next;
    struct ListNode* previous = head;
    while(temp != NULL){
        if(temp->val == previous->val){
            previous->next = temp->next;
        } else{
            previous = temp;
        }
        temp = temp->next;
    }
    return head;
}