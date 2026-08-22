import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
        start = 0
        end = len(clean_s) - 1
        while start < end:
            if clean_s[start] != clean_s[end]:
                return False
            start += 1
            end -= 1
        return True