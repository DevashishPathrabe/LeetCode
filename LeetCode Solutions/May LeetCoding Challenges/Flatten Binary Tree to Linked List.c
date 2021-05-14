/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


void flatten(struct TreeNode* root){
    struct TreeNode* head = NULL, *current = root;
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