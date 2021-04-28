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
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int>result;
        stack<TreeNode*>s;
        if(root == NULL){
            return result;
        }
        s.push(root);
        while(!s.empty()){
            if(root){
                result.push_back(root->val);
                s.push(root);
                root = root->left;
            }
            if(!root){
                TreeNode* current = s.top();
                s.pop();
                root = current->right;
            }
        }
        return result;
    }
};