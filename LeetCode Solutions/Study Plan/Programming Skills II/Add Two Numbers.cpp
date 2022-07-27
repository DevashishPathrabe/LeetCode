/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *Sum = new ListNode(0);
        ListNode *current = Sum;
        int carry = 0;
        while(l1 != NULL || l2 != NULL){
            if(l1 == NULL){
                l1 = new ListNode(0);
            }
            else if(l2 == NULL){
                l2 = new ListNode(0);
            }
            int addition = l1->val + l2->val + carry;
            if(addition >= 10){
                carry = 1;
                current->next = new ListNode(addition-10);
            }
            else{
                carry = 0;
                current->next = new ListNode(addition);
            }
            current = current->next;
            l1 = l1->next;
            l2 = l2->next;
        }
        if(carry > 0){
            current->next = new ListNode(carry);
        }
        return Sum->next;
    }
};