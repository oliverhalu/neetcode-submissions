from collections import deque 

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque()
        result = []
        for right in range(len(nums)):
            left = max(0,right - k + 1)
            # check if leftmost index is stale
            if len(deq) > 0:
                (window_max, index) = deq[0]
                if index < left:
                    deq.popleft()
                new_e = nums[right]
                while len(deq) != 0 and new_e > (deq[-1][0]):
                # while the incoming element is greater then the right most element, we have to pop
                    deq.pop()
            deq.append((nums[right],right))
            if right - left + 1 == k:
                result.append(deq[0][0])
        
        return result