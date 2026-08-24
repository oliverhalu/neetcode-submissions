class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq_so_far = 0
        left = 0
        count = {}
        max_length = 0
        for right in range(len(s)):
            # imo less readable:
            # count[s[right]] = coubt.get(s[right], 0) + 1
            if s[right] in count:
                count[s[right]] += 1
            else:
                count[s[right]] = 1
            max_freq_so_far = max(max_freq_so_far, count[s[right]])
            window_size = right - left + 1
            if window_size - max_freq_so_far > k:
                count[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        
        return max_length
