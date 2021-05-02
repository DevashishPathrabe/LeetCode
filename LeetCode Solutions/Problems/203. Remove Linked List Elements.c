/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* removeElements(struct ListNode* head, int val){
    struct ListNode *current = head;
    struct ListNode *previous = NULL;
    while(current != NULL){
        if(current->val == val){
            if(current == head){
                head = head->next;
                current = head;
            } else{
                previous->next = current->next;
                current = previous->next;
            }
        }
        else{
            previous = current;
            current = current->next;
        }
    }
    return head;
}