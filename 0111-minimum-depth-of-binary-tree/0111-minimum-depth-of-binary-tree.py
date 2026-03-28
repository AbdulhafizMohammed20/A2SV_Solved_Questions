# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: if the tree is empty
        if not root:
            return 0
        
        # Initialize queue for level-order traversal and current depth
        queue = deque([root])
        depth = 1
        
        while queue:
            # Number of nodes at the current level
            size = len(queue)
            
            for _ in range(size):
                node = queue.popleft()
                
                # If a leaf node is found, return the current depth immediately
                if not node.left and not node.right:
                    return depth
                
                # Add children to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Move to the next level
            depth += 1
            
        return depth