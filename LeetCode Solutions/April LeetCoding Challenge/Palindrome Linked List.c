/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


bool isPalindrome(struct ListNode* head){
    struct ListNode* slow = head;
    struct ListNode* fast = head;
    struct ListNode* previous = NULL;
    while(fast != NULL && fast->next != NULL){
        slow = slow->next;
        fast = fast->next->next;
    }
    previous = slow;
    slow = slow->next;
    previous->next = NULL;
    while(slow != NULL){
        struct ListNode* temp = slow->next;
        slow->next = previous;
        previous = slow;
        slow = temp;
    }
    fast = head;
    slow = previous;
    while(slow != NULL){
        if(fast->val != slow->val){
            return false;
        }
        fast = fast->next;
        slow = slow->next;
    }
    return true;
}