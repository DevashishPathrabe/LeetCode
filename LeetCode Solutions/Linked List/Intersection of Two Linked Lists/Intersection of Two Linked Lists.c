/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    struct ListNode *head1 = headA;
    struct ListNode *head2 = headB;
    while (head1 != head2){
        if (head1 == NULL){
            head1 = headB;
        } else{
            head1 = head1->next;
        }
        if (head2 == NULL){
            head2 = headA;
        } else{
            head2 = head2->next;
        }
    }
    return head1;
}