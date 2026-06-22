class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        median_dist = (m + n) // 2
        
        l, r = 0, m

        while l <= r:
            mid1 = (l+r) // 2
            mid2 = median_dist - mid1

            left1 = float('-inf') if mid1 == 0 else nums1[mid1-1]
            right1 = float('inf') if mid1 == m else nums1[mid1]

            left2 = float('-inf') if mid2 == 0 else nums2[mid2-1]
            right2 = float('inf') if mid2 == n else nums2[mid2]

            if left1 <= right2 and left2 <= right1:
                if (m+n)%2 == 1:
                    return min(right1, right2)
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2
            
            elif left1 > right2:
                r = mid1-1
            else:
                l = mid1+1