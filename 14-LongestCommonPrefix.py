class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if "" in strs:
            return ""

        pre = strs[0]
        max_match = len(pre)
        i = 1
        end = len(strs)
        while i < end and max_match > 0:
            if len(strs[i]) < max_match:
                max_match = len(strs[i])
                pre = pre[:max_match]

            if max_match > 0:
                for j in range(max_match):
                    if pre[j] != strs[i][j]:
                        pre = pre[:j]
                        max_match = j
                        break
            i += 1

        return pre


        
