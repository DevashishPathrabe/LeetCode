/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* deleteMiddle(struct ListNode* head){
    if (head->next == NULL){
        return head->next;
    }
    struct ListNode* fast = head->next->next;
    struct ListNode* slow = head;
    while (fast != NULL && fast->next != NULL){
        slow = slow->next;
        fast = fast->next->next;
    }
    slow->next = slow->next->next;
    return head;
}