class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # Two pointers
        i, j = 0, 0
        jump = 0
        jump_str = ""
        valid_nums = [str(i) for i in range(0, 10)]
        
        # While word finishes
        while i < len(word) and j < len(abbr):
            if abbr[j] in valid_nums:
                jump_str += abbr[j]
                j += 1

            elif jump_str != "":
                if jump_str[0] == "0":
                    return False

                jump = int(jump_str)
                jump_str = ""
                i += jump
                if i > len(word):
                    return False

            elif word[i] == abbr[j]:
                i += 1
                j += 1

            elif word[i] != abbr[j]:
                return False

        if jump_str != "" and jump_str[0] != "0":
            jump = int(jump_str)
            i += jump
                
        if j == len(abbr) and i == len(word):
            return True
        
        return False





        
