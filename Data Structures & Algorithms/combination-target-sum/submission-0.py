class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(path, start, remaining):
            if remaining == 0:
                result.append(path[:])
                return
            elif remaining < 0:
                return
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(path, i, remaining - nums[i])
                path.pop()
        backtrack([], 0, target)
        return result