class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0,0
        count = 1
        while fast <= len(nums):
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        reset = 0
        while reset != fast:
            reset = nums[reset]
            fast = nums[fast]

        return reset