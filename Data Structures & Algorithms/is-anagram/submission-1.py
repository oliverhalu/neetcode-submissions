class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # early exit if strings differ in length
        if len(s) != len(t): return False
        # iterate through strings 
        frequency_s = {}
        frequency_t = {}
        for i in range(len(s)):
            if s[i] in frequency_s:
                frequency_s.update({s[i]: frequency_s[s[i]]+1})
            else:
                frequency_s[s[i]] = 1
            if t[i] in frequency_t:
                frequency_t.update({t[i]: frequency_t[t[i]]+1})
            else:
                frequency_t[t[i]] = 1
        return frequency_s == frequency_t

