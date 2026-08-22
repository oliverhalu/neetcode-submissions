class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        left_max_arr = [0] * length
        running_max = 0
        for i in range(length):
            # if we are at the left border there is nothing so 0
            if i == 0:
                left_max_arr[i] = 0
            else:
                running_max = max(running_max, height[i-1])
                left_max_arr[i] = running_max
        
        right_max_arr = [0] * length
        running_max = 0
        for i in range(length-1, -1, -1):
            if i == length-1:
                right_max_arr[i] = 0
            else:
                running_max = max(running_max, height[i+1])
                right_max_arr[i] = running_max

        result = 0
        for i in range(length):
            water_at_i = max(0, (min(left_max_arr[i], right_max_arr[i]) - height[i]))
            result += water_at_i

        return result
                

        