import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        k = m + n
        if m < n:
            l_max, r_min = self.findPartitionPoints(nums1, nums2, k)
        else: 
            l_max, r_min = self.findPartitionPoints(nums2, nums1, k)

        if k % 2 == 0:
            return (l_max + r_min) / 2
        else: 
            return l_max

    def findPartitionPoints(self, search_array: List[int], compare_array: List[int], k: int) -> Tuple[int, int]: 
        l, r = 0, len(search_array)
        while l <= r:
            j = (l+r) // 2
            i = (k+1) // 2 - j
            l_1_max = search_array[j-1] if j > 0 else -math.inf
            r_1_min = search_array[j] if j <= len(search_array) - 1 else math.inf
            l_2_max = compare_array[i-1] if i > 0 else -math.inf
            r_2_min = compare_array[i] if i <= len(compare_array) - 1 else math.inf
            if l_1_max <= r_2_min and l_2_max <= r_1_min:
                return (max(l_1_max, l_2_max), min(r_1_min, r_2_min))
            elif l_1_max > r_2_min and l_2_max <= r_1_min:
                r = j - 1
            elif l_1_max <= r_2_min and l_2_max > r_1_min:
                l = j + 1

        