class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t.lstrip("-").isdigit():
                stack.append(int(t))
            else:
                operand_1 = stack.pop()
                operand_2 = stack.pop()
                match t:
                    case "+":
                        result = operand_2 + operand_1
                    case "-":
                        result = operand_2 - operand_1
                    case "*":
                        result = operand_2 * operand_1
                    case "/":
                        result = int(operand_2 / operand_1)
                stack.append(result)
        
        return int(stack[-1])