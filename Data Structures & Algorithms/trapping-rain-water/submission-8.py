class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        left = 0
        max_left = 0
        right = length - 1
        max_right = 0
        result = 0
        while left < right:
            if height[left] < height[right]:
                result += max(0, max_left - height[left])
                left += 1
                max_left = max(max_left, height[left-1])
            else:
                result += max(0, max_right - height[right])
                right -= 1
                max_right = max(max_right, height[right+1])
            
            

        return result
        
