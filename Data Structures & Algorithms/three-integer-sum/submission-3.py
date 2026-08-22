class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        print(nums)
        for i in range(len(nums)):
            if i != 0:
                if nums[i] == nums[i-1]:
                    continue
            current_sum = nums[i]
            start = i+1
            end = len(nums) - 1
            while start < end:
                if nums[start] + nums[end] + current_sum == 0:
                    if [nums[i],nums[start],nums[end]] not in output:
                        output.append([nums[i],nums[start],nums[end]])
                    start += 1
                elif nums[start] + nums[end] + current_sum < 0:
                    start += 1
                else:
                    end -= 1

        return output
