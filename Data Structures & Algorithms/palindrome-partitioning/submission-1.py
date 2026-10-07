class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        def backtrack(start, end, path):
            if start >= len(s):
                result.append(path[:])
                return

            for end in range(start, len(s)):
                l, r = start, end
                while l < r:
                    if s[l] != s[r]:
                        break
                    l += 1
                    r -= 1

                if l < r:
                    continue
                    return
                else:
                    path.append(s[start : end + 1])
                    backtrack(end + 1, len(s), path)
                    path.pop()
                    
                
                    

        backtrack(0, len(s), [])
        return result