/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


struct TreeNode* searchBST(struct TreeNode* root, int val){
    if (root == NULL){
        return NULL;
    }
    while (root != NULL){
        if (root->val == val){
            return root;
        }
        else if (val < root->val){
            root = root->left;
        } else{
            root = root->right;
        }
    }
    return NULL;
}