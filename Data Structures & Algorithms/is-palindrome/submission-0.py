import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0: return True
        clean_s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
        print(clean_s)
        return clean_s == clean_s[::-1]
        