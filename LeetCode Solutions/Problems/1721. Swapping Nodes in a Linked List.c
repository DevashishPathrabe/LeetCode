/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* swapNodes(struct ListNode* head, int k){
    struct ListNode *A = head, *B = head, *nodeK;
    for(int i=1; i<k; i++){
        A = A->next;
    }
    nodeK = A, A = A->next;
    while(A){
        A = A->next, B = B->next;
    }
    int temp = nodeK->val;
    nodeK->val = B->val, B->val = temp;
    return head;
}