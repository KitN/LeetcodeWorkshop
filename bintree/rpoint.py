from typing import *
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        # Every righmost node points to None by default
        # Every node with children: left points to right
        # Every node with grandchildren: left.right points to right.left
        pass
        # Do a traversal, flipping pointers as you go
        self.preTrav(root)

    def preTrav(self, root) -> List[int]:
        if root == None:
            return []
        serial = []
        left = self.preTrav(root.left)
        right = self.preTrav(root.right)
        self.linkup(root)

    def linkup(self, root) -> None:
        haskids, hasgrkids = False, False
        if root.left:
            haskids = True
            if root.left.left:
                hasgrkids = True
        if haskids: # Link the left to the right
            root.left.next = root.right
            #print(root.left.val, " points to ", root.right.val)
            if hasgrkids:
                root.left.right.next = root.right.left
                #print(root.left.right.val, " points to ", root.right.left.val)
        return("Has kids: ", haskids, "Has gkids: ", hasgrkids)
        

twig = Node(9, Node(6), Node(3))
bush = Node(8, Node(4), Node(2))
top = Node(10, twig, bush)
leaf = Node(1)

s = Solution()

ans = s.connect(top)
print(ans)
