/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public void flatten(TreeNode root) {
        TreeNode head = null, current = root;
        while(head != root){
            if(current.right == head){
                current.right = null;
            }
            if(current.left == head){
                current.left = null;
            }
            if(current.right != null){
                current = current.right;
            }
            else if(current.left != null){
                current = current.left;
            } else{
                current.right = head;
                head = current;
                current = root;
            }
        }
    }
}