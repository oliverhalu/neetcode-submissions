class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while len(stack) > 0 and t > stack[-1][0]:
                top_stack_index = stack[-1][1]
                result[top_stack_index] = i - top_stack_index
                stack.pop()
            stack.append((t,i))

        return result



        




        
        