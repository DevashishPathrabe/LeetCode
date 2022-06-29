/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* removeElements(struct ListNode* head, int val){
    struct ListNode *curr = head;
    struct ListNode *prev = NULL;
    while (curr != NULL){
        if (curr->val == val){
            if (curr == head){
                head = head->next;
                curr = head;
            } else{
                prev->next = curr->next;
                curr = prev->next;
            }
        }
        else{
            prev = curr;
            curr = curr->next;
        }
    }
    return head;
}