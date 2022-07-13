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
    ListNode* swapPairs(ListNode* head) {
        if (head == NULL){
            return NULL;
        }
        if (head->next == NULL){
            return head;
        }
        if (head->next->next == NULL){
            ListNode* newHeader = head->next;
            newHeader->next = head;
            head->next = NULL;
            return newHeader;
        }
        ListNode* nextPairHeader = head->next->next;
        ListNode* newHeader = head->next;
        newHeader->next = head;
        head->next = swapPairs(nextPairHeader);
        return newHeader;
    }
};