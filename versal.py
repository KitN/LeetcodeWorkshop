# Definition for a binary tree node.
from typing import Optional, List
import queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        lefty = []
        righty = []
        if root.left:
            lefty = self.preorderTraversal(root.left)
        if root.right:
            righty = self.preorderTraversal(root.right)
        return [root.val] + lefty + righty

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        lefty = []
        righty = []
        if root.left:
            lefty = self.preorderTraversal(root.left)
        if root.right:
            righty = self.preorderTraversal(root.right)
        return lefty + root.val + righty

    def levelSearch(self, root: Optional[TreeNode]) -> List[int]:
        levels = [[]]
        q = queue.Queue()
        q.put((root, 0))
        height = 0
        while not q.empty():
            eye = q.get()
            height = eye[1]
            node = eye[0]
            if eye[0]:
                try:
                    levels[height].append(node.val)
                except IndexError:
                    levels.append([])
                    levels[height].append(node.val)
                q.put((node.left, height +1))
                q.put((node.right, height +1))
        return levels

s = Solution()

base = TreeNode(1, TreeNode(2), TreeNode(3))
race = TreeNode(9, TreeNode(8), TreeNode(7))
left = TreeNode(2, TreeNode(4), TreeNode(5))
right = TreeNode(3, TreeNode(6), TreeNode(7))
top = TreeNode(1, left, right)

megabase= TreeNode(4, base, race)

print(s.levelSearch(top))
