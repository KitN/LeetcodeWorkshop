from typing import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None: # a 'None' leaf has no depth
            return 0
        #Maximum Depth is the greater of the left and right branch depths.
        leftd = self.maxDepth(root.left)
        rightd = self.maxDepth(root.right)
        newmax = max(leftd, rightd) + 1
        return newmax

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None: # An 'empty' leaf is the base case
            return True
        if root.right == None and root.left == None:
            return True # A simple leaf is symmetric
        elif root.right == None or root.left == None:
            return False # If either branch is dead, assymetry
        lrmirror = self.areMirror(root.left, root.right)
        if lrmirror: 
            return True
        else:
            return False

    def areMirror(self, left: Optional[TreeNode], right: Optional[TreeNode]):
        if left == None and right == None:
            return True # Base Case
        if left == None or right == None:
            return False
        outermirror = self.areMirror(left.left, right.right)
        innermirror = self.areMirror(left.right, right.left)
        headsequal = left.val == right.val
        return headsequal and outermirror and innermirror
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        if root.left == None and root.right == None:
            return root.val == targetSum
        remainder = targetSum - root.val
        lefthas = self.hasPathSum(root.left, remainder)
        righthas = self.hasPathSum(root.right, remainder)
        return lefthas or righthas

    def possibleTrees(self, inorder: List[int]) -> List[TreeNode]:
        """ Take the inorder traversal of a binary tree and return a list of
        possible trees by their roots."""
        possibles = []
        numnodes = len(inorder)
        if numnodes == 0: 
            return possibles
        if numnodes == 1:
            leaf = TreeNode(inorder[0])
            possibles = [leaf]
        for i in range(numnodes):
            # Slice the traversal into possible partitions
            leftslice = inorder[:i]
            root = inorder[i]
            rightslice = inorder[i+1:]
            # Generate possible trees for the sub-traversals
            leftps = self.possibleTrees(leftslice)
            rightps = self.possibleTrees(rightslice)
            for bro in leftps:
                for sis in rightps:
                    tree = TreeNode(root, bro, sis)
                    possibles.append(tree)
        return possibles


s = Solution()

oneleaf = TreeNode(1)
twoleaf = TreeNode(2)

twig = TreeNode(3, oneleaf, None)
branch = TreeNode(3, oneleaf, twoleaf)

tester = TreeNode(5, twig, branch)

travs = [[], [7], [2,3], [4,5,6]]

for t in travs:
    potentials = s.possibleTrees(t)
    for p in potentials:
        print(p)

