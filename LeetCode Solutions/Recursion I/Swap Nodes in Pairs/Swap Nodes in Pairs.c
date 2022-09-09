/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* swapPairs(struct ListNode* head){
    if (head == NULL){
        return NULL;
    }
    if (head->next == NULL){
        return head;
    }
    if (head->next->next == NULL){
        struct ListNode* newHeader = head->next;
        newHeader->next = head;
        head->next = NULL;
        return newHeader;
    }
    struct ListNode* nextPairHeader = head->next->next;
    struct ListNode* newHeader = head->next;
    newHeader->next = head;
    head->next = swapPairs(nextPairHeader);
    return newHeader;
}