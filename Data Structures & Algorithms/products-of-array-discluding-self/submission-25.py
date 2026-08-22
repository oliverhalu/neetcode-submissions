class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * len(nums)
        left = 1
        for i in range(n):
            output[i] = left
            left *= nums[i]
            
        # nums = [1,2,4,6] | nums = [-1,0,1,2,3]
        # output = [1,1,2,8] | output = [-1,0,0,0,0]
        right = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right
            right *= nums[i]
            

        return output

