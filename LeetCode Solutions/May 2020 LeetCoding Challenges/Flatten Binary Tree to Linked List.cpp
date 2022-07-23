/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void flatten(TreeNode* root) {
        TreeNode* head = NULL, *current = root;
        while(head != root){
            if(current->right == head){
                current->right = NULL;
            }
            if(current->left == head){
                current->left = NULL;
            }
            if(current->right != NULL){
                current = current->right;
            }
            else if(current->left != NULL){
                current = current->left;
            } else{
                current->right = head;
                head = current;
                current = root;
            }
        }
    }
};