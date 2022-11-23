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
    int minCameraCover(TreeNode* root) {
        return helper(root) > 2 ? minNumberOfCameras + 1 : minNumberOfCameras;
    }
    int helper(TreeNode* node) {
        if(!node){
            return 0;
        }
        int value = helper(node->left) + helper(node->right);
        if(value == 0){
            return 3;
        }
        if(value < 3){
            return 0;
        }
        minNumberOfCameras++;
        return 1;
    }
private:
    int minNumberOfCameras = 0;
};