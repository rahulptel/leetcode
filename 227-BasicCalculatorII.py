from collections import deque

class Solution:
    def calculate(self, s: str) -> int:   
        # Remove spaces and add a dummy "+" operation in the end to handle last number
        # in the string
        s = s.replace(" ", "") + "+"
        
        prev_op = "+"
        num = 0
        stack = deque()
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            else:
                if prev_op == "+":
                    stack.append(num)
                
                elif prev_op == "-":
                    stack.append(-num)

                elif prev_op == "*":
                    stack.append(int(stack.pop() * num))
                    
                elif prev_op == "/":
                    stack.append(int(stack.pop() / num))
                
                prev_op = ch
                num = 0 

        return sum(stack)
