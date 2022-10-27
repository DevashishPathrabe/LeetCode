class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        img1_points, img2_points, d = [], [], collections.defaultdict(int)
        for r in range(len(img1)):
            for c in range(len(img1[0])):
                if img1[r][c]:
                    img1_points.append((r, c))
                if img2[r][c]:
                    img2_points.append((r, c))
        for r_a, c_a in img1_points:
            for r_b, c_b in img2_points:
                d[(r_b - r_a, c_b - c_a)] += 1
        return max(d.values() or [0])