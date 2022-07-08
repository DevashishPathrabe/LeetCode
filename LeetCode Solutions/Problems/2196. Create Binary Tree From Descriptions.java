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
    public TreeNode createBinaryTree(int[][] descriptions) {
        Map<Integer,TreeNode> map = new HashMap<>();
        Set<Integer> set = new HashSet<>();
        for (int[] des:descriptions){
            int parent = des[0];
            int child = des[1];
            TreeNode childNode = map.getOrDefault(child,new TreeNode(child));
            TreeNode parentNode  =  map.getOrDefault(parent,new TreeNode(parent));
            if (des[2] == 0){
                parentNode.right = childNode;
            }
            else {
                parentNode.left = childNode;
            }
            map.put(child, childNode);
            map.put(parent, parentNode);
            set.add(child);
        }
        for (Integer key:map.keySet()) {
            if (!set.contains(key)) {
                return map.get(key);
            }
        }
        return null;
    }
}