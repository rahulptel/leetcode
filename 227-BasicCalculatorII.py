from collections import deque

class Solution:
    def calculate(self, s: str) -> int:        
        scratch = ""
        q = deque([])        
        sign="+"

        s = "".join(s.strip().split(" "))

        i = 0
        # Iterate over string   
        while i < len(s):
            ch = s[i]
            # If char is * or /. add num in scratch to stack with sign
            if ch == "/" or ch == "*":    
                if len(scratch):
                    if sign == "+":
                        q.append(int(scratch))
                    else:
                        q.append(-int(scratch))
                    sign = "+"

                op = ""
                i += 1
                while i < len(s) and s[i].isdigit():                    
                    op += s[i]
                    i += 1

                op1 = q.pop()
                
                if ch == "/":                    
                    result = int(op1 / int(op))                    
                else:
                    result = op1 * int(op)
                
                # Push the result in the stack
                if sign == "+":
                    q.append(result)
                else:
                    q.append(-result)

                scratch = ""
                continue

            # If char is + or -, add num in scratch to stack with sign
            elif ch == "+" or ch == "-":            
                if len(scratch):
                    if sign == "+":
                        q.append(int(scratch))
                    else:
                        q.append(-int(scratch))

                sign = ch
                scratch = ""

            # Read char and store result in scratch
            else:                
                scratch += ch        
            i += 1
        
        if len(scratch):
            if sign == "+":
                q.append(int(scratch))
            elif sign == "-":
                q.append(-int(scratch))

        # If end of string, pop all elements and add
        result = 0
        while len(q):
            result += q.pop()

        return result
        
