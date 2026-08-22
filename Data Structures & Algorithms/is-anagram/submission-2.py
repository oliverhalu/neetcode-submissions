class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # early exit if strings differ in length
        if len(s) != len(t): return False
        # iterate through strings 
        frequency_s = {}
        frequency_t = {}
        for i in range(len(s)):
            frequency_s[s[i]] = frequency_s.get(s[i], 0) + 1
            frequency_t[t[i]] = frequency_t.get(t[i], 0) + 1
            
        return frequency_s == frequency_t

