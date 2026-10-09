class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        length = sum(matchsticks) // 4
        sides = [0] * 4

        if sum(matchsticks) % 4 != 0:
            return False

        matchsticks.sort(reverse = True)

        def backtrack(start):
            if start == len(matchsticks):
                return True

            for i in range(4):
                if sides[i] + matchsticks[start] <= length:
                    sides[i] += matchsticks[start]

                    if backtrack(start + 1):
                        return True

                    sides[i] -= matchsticks[start]

            return False

        return backtrack(0)
