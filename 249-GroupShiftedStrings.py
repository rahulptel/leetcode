class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        hashmap = {}

        for string in strings:
            if len(string) == 1:
                key = ""
            else:    
                key_list = []
                for i in range(0, len(string) - 1):                    
                    key_list.append(((ord(string[i + 1]) - ord(string[i])) % 26) + ord('a'))
                key = "".join(list(map(str, key_list)))

            if key in hashmap:
                hashmap[key].append(string)
            else:
                hashmap[key] = [string]

        return list(hashmap.values())

        
