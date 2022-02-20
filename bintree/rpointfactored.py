from typing import *
#import pudb; pu.db
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return None
        self.preTrav(root)
        return root

    def preTrav(self, root) -> List[int]:
        if root == None:
            return
        left = self.preTrav(root.left)
        right = self.preTrav(root.right)
        self.linkup(root)

    def linkup(self, root) -> None:
        ndepth = self.depth(root)
        for n in range(1,ndepth+1):
            bro = root.left
            sis = root.right
            repeat = n
            while repeat > 1:
                bro = bro.right
                sis = sis.left
                repeat -= 1
            bro.next = sis


    def depth(self, root) -> int:
        count = 0
        while root.left:
            root = root.left
            count += 1
        return count


leafdict = dict()
# Make loose leaves with distinct values, hashed by their values
for n in range(1,17):
    leaf = Node(n)
    leafdict[n] = leaf

# Link them up
for k in range(1,7+1):
    node = leafdict[k]
    node.left = leafdict[k*2]
    node.right = leafdict[k*2+1]

s = Solution()

s.connect(leafdict[1])

