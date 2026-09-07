class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i,e in enumerate(heights):
            start = i
            while stack and stack[-1][0] > e:
                popped_height, popped_start = stack.pop()
                area = popped_height * (i - popped_start)
                max_area = max(max_area, area)
                start = popped_start
            stack.append((e,start))

        
        while len(stack) > 0:
            top = stack.pop()
            area = (len(heights) - top[1]) * top[0]
            max_area = max(max_area, area)


        return max_area

                          
     
  