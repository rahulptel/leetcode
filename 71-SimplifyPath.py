from collections import deque

class Solution:
    def simplifyPath(self, path: str) -> str:
        subpaths = path.strip().split("/")

        result = deque([])
        for sp in subpaths:
            if sp == "" or sp == ".":
                continue
            elif sp == "..":
                if len(result):
                    result.pop()
            else:
                result.append(sp)

        return "/" + "/".join(result)
            
