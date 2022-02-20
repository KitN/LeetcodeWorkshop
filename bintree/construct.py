from typing import *
from binarytree import tree, Node
import pudb; pu.db

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int])-> Optional[Node]:
        if postorder == []:
            return None
        candidates = self.postPoss(postorder)
        for can in candidates:
            io = self.inorderTraversal(can)
            if io == inorder:
                return can


    def postPoss(self, postorder: List[int]) -> List[Node]:
        """ Given a postorder traversal of a tree, construct a list containing
        all the possible trees (indexed by their root)"""
        poss = []
        numnodes = len(postorder)
        if postorder == []:
            poss.append(None)
            return poss
        rootval = postorder[-1] # The root node always has the last value
        if numnodes == 1:
            poss.append(Node(rootval))
            return poss
        for i in range(len(postorder)):
            leftslice = postorder[:i]
            rightslice = postorder[i:-1]
            lposs = self.postPoss(leftslice)
            rposs = self.postPoss(rightslice)
            for bro in lposs:
                for sis in rposs:
                    fam = Node(rootval, left=bro, right=sis)
                    poss.append(fam)
        return poss

    def inorderTraversal(self, root: Optional[Node]) -> List[int]:
        if root == None:
            return []
        lefty = []
        righty = []
        if root.left:
            lefty = self.inorderTraversal(root.left)
        if root.right:
            righty = self.inorderTraversal(root.right)
        return lefty + [root.value] + righty

# Testing
s = Solution()
## Make some test cases
emptyverse = []
oneval = [9]
twovals = [1,2]
threevals = [4,5,6]
fourvals = [3,5,7,11]

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

answer = s.buildTree(inorder, postorder)
print(answer)
