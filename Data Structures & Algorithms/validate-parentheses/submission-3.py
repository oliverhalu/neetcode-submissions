class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        counterparts = {")": "(", "}": "{", "]": "["}
        for e in s:
            if e == "(" or e == "{" or e == "[":
                stack.append(e)
            else:
                if len(stack) == 0:
                    return False
                last_e = stack[-1]
                if last_e == counterparts[e]:
                    stack.pop()
                else:
                    return False


        return len(stack) == 0