/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* reverseList(struct ListNode* head){
    struct ListNode *previous = NULL;
    struct ListNode *current = head ;     
    while(current != NULL){
        head = current;
        current = current->next;
        head->next = previous;
        previous = head;
    }
    return head;
}