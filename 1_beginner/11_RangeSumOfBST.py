# https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        curVal = root.val if low <= root.val <= high else 0

        leftSum = self.rangeSumBST(root.left, low, high)
        rightSum = self.rangeSumBST(root.right, low, high)

        return curVal + leftSum + rightSum

# 예시 트리 생성
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)

# Solution 객체 생성 및 함수 호출
sol = Solution()
low = 7
high = 15
result = sol.rangeSumBST(root, low, high)
print(result)  # 출력: 32