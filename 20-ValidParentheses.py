class Solution:
    def isValid(self, s: str) -> bool:
        stack = [s[0]]
        for i in s[1:]:
            if len(stack) and \
                ((i == '}' and stack[-1] == '{') or \
                (i == ')' and stack[-1] == '(') or \
                (i == ']' and stack[-1] == '[')):
                    stack.pop()
            else:
                stack.append(i)

        return len(stack) == 0
