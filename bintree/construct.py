from typing import *
from binarytree import tree, Node
#import pudb; pu.db

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int])-> Optional[Node]:
        if postorder == []:
            return None
        if len(postorder) == 1: # We have a leaf
            return Node(postorder[0])
        tailval = postorder[-1]
        rootnode = Node(tailval)
        keystone = inorder.index(tailval) # The index of tailval in the inorder
        leftwing = inorder[:keystone]
        rightwing = inorder[keystone+1:]
        # Find the corresponding slices of the postorder sequence
        leftwide = len(leftwing)
        rightwide = len(rightwing)
        lcomp = postorder[:leftwide]
        rcomp = postorder[leftwide:-1]
        # Recursively call the function to make the left and right subtrees.
        lsubtree = self.buildTree(leftwing, lcomp)
        rsubtree = self.buildTree(rightwing, rcomp)
        rootnode.left = lsubtree
        rootnode.right = rsubtree
        return(rootnode)

    def buildTreePre(self, preorder: List[int], inorder: List[int])-> Optional[Node]:
        if preorder == []:
            return None
        if len(preorder) == 1: # We have a leaf
            return Node(preorder[0])
        mouthval = preorder[0]
        rootnode = Node(mouthval)
        keystone = inorder.index(mouthval) # The index of mouthval in the inorder
        leftwing = inorder[:keystone]
        rightwing = inorder[keystone+1:]
        # Find the corresponding slices of the postorder sequence
        leftwide = len(leftwing)
        rightwide = len(rightwing)
        remaind = preorder[1:]
        lcomp = remaind[:leftwide]
        rcomp = remaind[leftwide:]
        # Recursively call the function to make the left and right subtrees.
        lsubtree = self.buildTreePre(lcomp, leftwing)
        rsubtree = self.buildTreePre(rcomp, rightwing)
        rootnode.left = lsubtree
        rootnode.right = rsubtree
        return(rootnode)


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
preorder = [3, 9, 20, 15, 7]

answer = s.buildTreePre(preorder, inorder)
print(answer)
