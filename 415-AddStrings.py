class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = ""

        carry = 0
        i, j = len(num1) - 1, len(num2) - 1
        
        while i >= 0 or j >= 0:
            n1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            n2 = ord(num2[j]) - ord('0') if j >= 0 else 0

            sum_ = n1 + n2 + carry
            value = sum_ % 10
            carry = sum_ // 10

            result = str(value) + result 
            i -= 1
            j -= 1
 
        if carry:
            result = str(carry) + result

        return result
        
