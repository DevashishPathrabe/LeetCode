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
    bool isSymmetric(TreeNode* root) {
        if (root == NULL){
            return true;
        }
        return isSymmetric(root,root);
    }
    bool isSymmetric(TreeNode* a, TreeNode* b){
        if (a == NULL && b == NULL){
            return true;
        }
        if (a != NULL && b != NULL && a->val == b->val){
            return isSymmetric(a->left, b->right) && isSymmetric(a->right, b->left);
        }
        return false;
    }
};