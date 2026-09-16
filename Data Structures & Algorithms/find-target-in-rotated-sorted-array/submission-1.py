class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            # case: right is sorted
            elif nums[mid] < nums[right]:
                # target is in right
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                # target is in left half
                else:
                    right = mid
            # case: left is sorted
            else:
                # target is in left half
                if nums[left] <= target < nums[mid]:
                    right = mid
                # target is in right half
                else:
                    left = mid + 1
        
        return -1
