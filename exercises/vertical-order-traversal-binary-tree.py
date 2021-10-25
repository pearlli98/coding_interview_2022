#https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        columnTable = defaultdict(list)
        min_col = max_col = 0
        
        def dfs(node, r, c):
            if node:
                columnTable[c].append((r, node.val))
                nonlocal min_col, max_col
                min_col = min(min_col, c)
                max_col = max(max_col, c)
                dfs(node.left, r + 1, c - 1)
                dfs(node.right, r + 1, c + 1)
        
        dfs(root, 0, 0)
        
        result = []
        for col in range(min_col, max_col + 1):
            result.append([val for row, val in sorted(columnTable[col])])
        
        return result
            
        