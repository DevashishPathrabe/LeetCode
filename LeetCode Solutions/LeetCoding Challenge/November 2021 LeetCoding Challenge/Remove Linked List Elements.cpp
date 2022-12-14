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
    ListNode* removeElements(ListNode* head, int val) {
        ListNode *current = head;
        ListNode *previous = NULL;
        while(current != NULL){
            if(current->val == val){
                if(current == head){
                    head = head->next;
                    current = head;
                } else{
                    previous->next = current->next;
                    current = previous->next;
                }
            }
            else{
                previous = current;
                current = current->next;
            }
        }
        return head;
    }
};