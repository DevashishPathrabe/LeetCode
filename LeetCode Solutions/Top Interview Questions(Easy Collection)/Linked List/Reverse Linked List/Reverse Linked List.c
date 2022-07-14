/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* reverseList(struct ListNode* head){
    struct ListNode *prev = NULL;
    struct ListNode *curr = head ;     
    while (curr != NULL){
        head = curr;
        curr = curr->next;
        head->next = prev;
        prev = head;
    }
    return head;
}