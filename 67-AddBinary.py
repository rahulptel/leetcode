class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        c = "0"
        result = ""

        while i >= 0 or j >= 0:
            count = 0
            if i >= 0:
                if a[i] == "1":
                    count += 1
                i -= 1

            if j >= 0:
                if b[j] == "1":
                    count += 1
                j -= 1

            if c == "1":
                count += 1

            if count == 3 or count == 1:
                result = "1" + result
            else:
                result = "0" + result
            
            if count >= 2: 
                c = "1"
            else:
                c = "0"

            

        if c == "1":
            return "1" + result

        return result


