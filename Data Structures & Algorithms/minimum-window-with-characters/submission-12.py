class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # build count map
        count_t = {}
        for e in t:
            count_t[e] = count_t.get(e, 0) + 1
        required = sum(list(count_t.values()))
        left = 0
        result = ""
        for right in range(len(s)):
            # progress right if char is in t and adapt count and required
            c = s[right]
            if c in count_t:
                count_t[c] -= 1
                if count_t[c] >= 0:
                    required -= 1
            while required == 0:
                if result == "" or right - left + 1 < len(result):
                    result = s[left:right + 1]
                lc = s[left]
                if lc in count_t:
                    count_t[lc] += 1
                    if count_t[lc] > 0:
                        required += 1
                left += 1
            
        return result

        
        

        