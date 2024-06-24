# https://leetcode.com/problems/minimum-number-game/description/

from typing import List

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        answer = []
        for i in range(len(nums)//2):
            answer += [nums[2 * i + 1], nums[2 * i]]
        return answer

solution = Solution()
print(solution.numberGame([5,4,2,3]))