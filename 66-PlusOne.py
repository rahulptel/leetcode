class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        k = len(digits) - 1
        flag = False
        while k >= 0:
            sum = digits[k] + carry            
            rem = sum % 10
            quo = sum // 10

            digits[k] = rem
            if quo > 0:
                carry = quo
            else:
                flag = True
                break
                
            k -= 1

        if not flag:
            digits.insert(0, quo)

        return digits
                
