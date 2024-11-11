class Solution:
    def romanToInt(self, s: str) -> int:
        roman2int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        i = 0
        total = 0
        while i < len(s):
            ch = s[i]
            if ch == "I":
                if i + 1 < len(s) and s[i+1] in "VX":                        
                    total += roman2int[s[i+1]] - 1
                    i += 1
                else:
                    total += 1

            elif ch == "X" and i + 1 < len(s):
                if i + 1 < len(s) and s[i+1] in "LC":                        
                    total += roman2int[s[i+1]] - 10
                    i += 1
                else:
                    total += 10
                
            elif ch == "C" and i + 1 < len(s):
                if i + 1 < len(s) and s[i+1] in "DM":                        
                    total += roman2int[s[i+1]] - 100
                    i += 1
                else:
                    total += 100

            else:
                total += roman2int[s[i]]

            i += 1

        return total
