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
    int countNodes(ListNode* head) {
        int n = 0;
        while (head){
            n++;
            head = head->next;
        }
        return n;
    }
    vector<ListNode*> splitListToParts(ListNode* head, int k){
        int n = countNodes(head);
        int part_size = n / k, left = n % k;
        ListNode *ptr = head, *previous = NULL;
        vector<ListNode*> result(k);
        for (int i=0; i<k; i++){
            result[i] = head;
            for (int j=0; j<part_size + (i < left); j++){
                previous = head;
                head = head->next;
            }
            if (previous){
                previous->next = NULL;
            }
        }
        return result;
    }
};