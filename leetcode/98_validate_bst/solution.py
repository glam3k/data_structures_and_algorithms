# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isValidBSTHelper(root: Optional[TreeNode]):
            if root is None:
                return True, None, None

            left_valid, left_min, left_max = isValidBSTHelper(root.left)
            right_valid, right_min, right_max = isValidBSTHelper(root.right)


            greater_than_left = left_max is None or root.val > left_max
            less_than_right = right_min is None or root.val < right_min

            result = left_valid and right_valid and greater_than_left and less_than_right

            minimum = min(root.val, left_min) if left_min else root.val
            maximum = max(root.val, right_max) if right_max else root.val

            return result, minimum, maximum

        result, _, _ = isValidBSTHelper(root)
        return result

    """
    Notes: 
    Don't get tricky with the math. Handle null and edge cases explicitly.

    """
