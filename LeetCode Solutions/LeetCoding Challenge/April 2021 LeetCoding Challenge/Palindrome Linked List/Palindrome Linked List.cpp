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
    bool isPalindrome(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        ListNode* previous = NULL;
        while (fast != NULL && fast->next != NULL){
            slow = slow->next;
            fast = fast->next->next;
        }
        previous = slow;
        slow = slow->next;
        previous->next = NULL;
        while (slow != NULL){
            ListNode* temp = slow->next;
            slow->next = previous;
            previous = slow;
            slow = temp;
        }
        fast = head;
        slow = previous;
        while (slow != NULL){
            if (fast->val != slow->val){
                return false;
            }
            fast = fast->next;
            slow = slow->next;
        }
        return true;
    }
};