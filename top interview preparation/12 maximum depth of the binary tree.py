# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0; 
        else:
            leftheight = self.maxDepth(root.left);
            rightheight = self.maxDepth(root.right);    
            
            return leftheight + 1 if leftheight > rightheight else rightheight + 1;      
        

        
        