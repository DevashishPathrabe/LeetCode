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
        if(head == NULL || head->next == NULL){
            return true;
        }
        ListNode *slow = head;
        ListNode *fast = head;
        while(fast != NULL && fast->next != NULL){
            slow = slow->next;
            fast = fast->next->next;
        }
        slow = reverseList(slow);
        fast = head;
        while(slow != NULL){
            if(slow->val != fast->val){
                return false;
            }
            slow = slow->next;
            fast = fast->next;
        }
        return true;
    }
    public:
        ListNode* reverseList(ListNode* node){
        ListNode *current = node;
        ListNode *previous = NULL;
        while(current != NULL){
            ListNode *currentNext = current->next;
            current->next = previous;
            previous = current;
            current = currentNext;
        }
        return previous;
    }
};