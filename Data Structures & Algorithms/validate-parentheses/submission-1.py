class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for e in s:
            if e == "(" or e == "{" or e == "[":
                stack.append(e)
            else:
                # closing bracket
                if len(stack) == 0:
                    return False
                last_e = stack[-1]
                if e == ")":
                    if last_e == "(":
                        stack.pop()
                    else:
                        return False
                elif e == "}":
                    if last_e == "{":
                        stack.pop()
                    else:
                        return False
                elif e == "]":
                    if last_e == "[":
                        stack.pop()
                    else:
                        return False

        return len(stack) == 0