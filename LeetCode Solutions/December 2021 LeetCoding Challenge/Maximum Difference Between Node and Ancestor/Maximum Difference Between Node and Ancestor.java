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
    int maxDiff = 0;
    public int maxAncestorDiff(TreeNode root) {
        helper(root, root.val, root.val);
        return maxDiff;
    }
    public void helper(TreeNode root, int min, int max) {
        if (root == null){
            return;
        }
        if (root.val > max) {
            max = root.val;
            maxDiff = Math.max(maxDiff, Math.abs(min-max));
        }
        if (root.val < min){
            min = root.val;
            maxDiff = Math.max(maxDiff, Math.abs(max - min));
        }
        helper(root.left, min, max);
        helper(root.right, min, max);
    }
}