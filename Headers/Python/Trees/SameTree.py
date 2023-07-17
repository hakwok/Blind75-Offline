from typing import Optional
import os

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return False
    
print(os.getcwd())
bob = os.getcwd()
cat = "Headers\Python\Arrays & Hashing\ContainsDuplicate.py"
talk = os.path.join(bob, cat)
print(talk)