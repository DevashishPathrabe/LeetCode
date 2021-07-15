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
    void reorderList(ListNode* head) {
        if(!head){
            return;
        }
        ListNode *temp = head, *half = head, *previous = NULL;
        while(temp->next && temp->next->next){
            temp = temp->next->next;
            half = half->next;
        }
        if(temp->next){
            half = half->next;
        }
        while(half){
            temp = half->next;
            half->next = previous;
            previous = half;
            half = temp;
        }
        half = previous;
        while(head && half){
            temp = head->next;
            previous = half->next;
            head->next = half;
            half->next = temp;
            head = temp;
            half = previous;
        }
        if(head && head->next){
            head->next->next = NULL;
        }
    }
};