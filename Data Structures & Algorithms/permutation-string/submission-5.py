class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        for c in s1:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        original_count = count.copy()
        left = 0
        right = 0 
        while right < len(s2):
            print(count)
            if s2[right] in count: 
                if count[s2[right]] == 0:
                    count[s2[left]] += 1
                    left += 1
                else: 
                    count[s2[right]] -= 1
                    right += 1
                if all(v == 0 for v in count.values()): return True
            else: 
                left = right + 1
                count = original_count.copy()
                right += 1
        
        return False
