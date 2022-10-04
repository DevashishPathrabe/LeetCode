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
    int x = 4;
    public void dfs(TreeNode n, int sum){
        if (n == null){
            return;
        }
        if (n.left == null & n.right == null){
            if (sum-n.val == 0){
                x = 0;
            }
        } else{
            dfs(n.left, sum-n.val);
            dfs(n.right, sum-n.val);
        }
    }
    public boolean hasPathSum(TreeNode root, int totalSum) {
        dfs(root, totalSum);
        return x == 0;
    }
}