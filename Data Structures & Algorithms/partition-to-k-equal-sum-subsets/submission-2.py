class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        result = []
        target = sum(nums) / k
        used = [False] * len(nums)

        def backtrack(start, k, subsetSum):
            if k == 0:  
                return True
            
            if subsetSum == target:
                return backtrack(0, k - 1, 0)

            for i in range(start, len(nums)):
                if used[i] or subsetSum + nums[i] > target:
                    continue

                used[i] = True

                if backtrack(i + 1, k, subsetSum + nums[i]):
                    return True

                used[i] = False

            return False

        return backtrack(0, k, 0)