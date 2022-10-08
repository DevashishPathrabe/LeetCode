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
    private int minNumberOfCameras = 0;
    public int minCameraCover(TreeNode root) {
        return helper(root) > 2 ? minNumberOfCameras + 1 : minNumberOfCameras;
    }
    public int helper(TreeNode node) {
        if (node == null){
            return 0;
        }
        int value = helper(node.left) + helper(node.right);
        if (value == 0){
            return 3;
        }
        if (value < 3){
            return 0;
        }
        minNumberOfCameras++;
        return 1;
    }
}