# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return [head[::-1]]

    def test(self, t):
        rev = self.reverseList(t[0])
        if rev == t[1]:
            print(t, 'Pass', sep='\t')
        else:
            print(t, 'Fail', sep='\t')
        

t1 = [1,2]
t1r = [2,1]
empty = []
emptyr = []
t2 = [4,5,6,7]
t2r = [7,6,5,4]
tests = [(t1,t1r),(empty,emptyr),(t2,t2r)]

s = Solution()
for tes in tests:
    print(tes)
    s.test(tes)
