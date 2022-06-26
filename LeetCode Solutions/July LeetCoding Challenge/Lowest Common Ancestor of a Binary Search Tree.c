/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q) {
    int small = fmin(p->val, q->val);
    int large = fmax(p->val, q->val);
    while(root != NULL){
        if(root->val > large){
            root = root->left;
        }
        else if(root->val < small){
            root = root->right;
        }
        else{
            return root;
        }
    }
    return NULL;
}