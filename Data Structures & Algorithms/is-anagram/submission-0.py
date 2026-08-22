class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for c in s:
            if c not in t:
                return False
            else:
                s_index = s.index(c)
                t_index = t.index(c)
                s = s[:s_index] + s[s_index + 1:]
                t = t[:t_index] + t[t_index + 1:]
        return True

