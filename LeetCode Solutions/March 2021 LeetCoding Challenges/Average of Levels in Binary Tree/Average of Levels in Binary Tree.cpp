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
    vector<double> averageOfLevels(TreeNode* root) {
        queue<TreeNode*> queue;
        queue.push(root);
        vector<double> averageValue;
        while (queue.size()){
            double queueLength = queue.size(), row = 0;
            for (int i=0; i<queueLength; i++){
                TreeNode* current = queue.front(); 
                queue.pop();
                row += current->val;
                if (current->left){
                    queue.push(current->left);
                }
                if (current->right){
                    queue.push(current->right);
                }
            }
            averageValue.push_back(row/queueLength);
        }
        return averageValue;
    }
};