class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        def backtracking(index, subset):
            nonlocal res
            xor_sum = 0  
            for num in subset:
                xor_sum ^= num
            res += xor_sum

            for j in range(index, len(nums)):
                subset.append(nums[j])
                backtracking(j + 1, subset)
                subset.pop()
        
        backtracking(0, [])
        return res