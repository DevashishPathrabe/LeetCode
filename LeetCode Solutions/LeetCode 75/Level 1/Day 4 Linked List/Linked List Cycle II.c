/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *detectCycle(struct ListNode *head) {
    struct ListNode *slow = head;
    struct ListNode *fast = head;
    while(fast && fast->next){
        fast = fast->next->next;
        slow = slow->next;
        if(slow == fast){
            slow = head;
            while(slow){
                if(slow == fast){
                    return slow;
                }
                slow = slow->next;
                fast = fast->next;
            }
        }
    }
    return NULL;
}