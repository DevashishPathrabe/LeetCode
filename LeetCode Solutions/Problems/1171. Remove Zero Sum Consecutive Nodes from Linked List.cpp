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
    ListNode* removeZeroSumSublists(ListNode* head) {
        ListNode node(0);
        ListNode* nodeV = &node;
        nodeV->next = head;
        ListNode* headA = nodeV;
        unordered_map<int, ListNode* > d;
        vector<int> dv;
        int s = 0;
        while (nodeV){
            s += nodeV->val;
            if (d.count(s) == 0){
                d[s] = nodeV;
                dv.push_back(s);
            } else {
                d[s]->next = nodeV->next;
                while (dv.back() != s){
                    int t = dv.back();
                    dv.pop_back();
                    d.erase(t);
                }
            }
            nodeV = nodeV->next;
        }
        return headA->next;
    }
};