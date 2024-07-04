# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/

from typing import List
from itertools import combinations

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        combi = list(combinations(nums, 2))
        filtered_combi = list(filter(lambda x: x[0] + x[1] < target, combi))
        result = len(filtered_combi)
        return result


nums = [-1,1,2,3,1]
target = 2
solution = Solution()
print(solution.countPairs(nums, target))