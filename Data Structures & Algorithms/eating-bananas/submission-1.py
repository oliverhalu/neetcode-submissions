class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        min_k = right

        while left <= right:
            mid = (left+right) // 2
            hours_needed = 0  
            for e in piles:
                hours_needed += math.ceil(e / mid)
            
            if hours_needed <= h:
                right = mid - 1
                min_k = min(min_k, mid)
            else:
                left = mid + 1
        
        return min_k