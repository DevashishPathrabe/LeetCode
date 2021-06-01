class Solution {
    public int[] advantageCount(int[] nums1, int[] nums2) {
        Integer[] order = new Integer[nums2.length];
        int[] permutation = new int[nums1.length];
        for(int i=0; i<nums2.length; i++){
            order[i] = i;
        }
        Arrays.sort(order, (a,b) -> Integer.compare(nums2[b], nums2[a]));
        Arrays.sort(nums1);
        int i = 0, j = nums2.length-1;
        for(int ix : order){
            permutation[ix] = nums1[j] > nums2[ix] ? nums1[j--] : nums1[i++];
        }
        return permutation;
    }
}