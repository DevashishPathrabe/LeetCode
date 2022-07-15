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
    public boolean isValidBST(TreeNode root) {
        return isValidBST(root,Long.MAX_VALUE,Long.MIN_VALUE);
    }
    public boolean isValidBST(TreeNode root,long min,long max){
        if(root == null)
            return true;
        if(root.val >= min || root.val <= max)
            return false;
        return isValidBST(root.left,root.val,max) && isValidBST(root.right,min,root.val);
    }
}