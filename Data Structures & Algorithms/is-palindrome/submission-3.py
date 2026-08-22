class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0: return True
        clean_s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
        print(clean_s)
        start = 0
        end = len(clean_s) - 1
        while start < end:
            print(start,end)
            if clean_s[start] != clean_s[end]:
                return False
            start += 1
            end -= 1
        return True