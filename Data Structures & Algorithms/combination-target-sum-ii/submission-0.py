class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        
        def backtrack(i, path, remaining):
            if remaining == target:
                result.append(path[:])
                return
            if remaining > target or i == len(candidates):
                return

            path.append(candidates[i])
            backtrack(i + 1, path, remaining + candidates[i])
            path.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, path, remaining)

        backtrack(0, [], 0)
        return result