from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        highscore = 0
        acc = 0
        for bit in nums:
            if bit == 1:
                acc += 1
                highscore = max(highscore, acc)
            else:
                acc = 0
        return highscore

    def howManyDigits(self, num: int) -> int:
        numdigits = 1
        for power in range(1,6):
            digit = num // 10**power
            if digit == 0:
                return numdigits
            numdigits += 1

    def evenDigCount(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if num // 10 and not num // 100:
                count += 1
                continue
            elif num // 1000 and not num // 10000:
                count += 1
                continue
            elif num // 100000:
                count += 1
            else:
                continue
        return count

    def fastEvenCount(self, nums: List[int]) -> int:
        acc = 0
        for n in nums:
            count = 1
            while n // 10 > 0:
                n = n // 10
                count += 1
            if count % 2 == 0:
                acc += 1
        return acc

    def countsquares(self, nums: List[int]) -> int:
        cubbies = [0 for x in range(10**4+1)]
        outlist = []
        for num in nums:
            val = abs(num)
            cubbies[val] += 1
        for i, cub in enumerate(cubbies):
            outlist += [i**2]*cub
        return outlist

    def merge(self, nums1, nums2):
        i = 0
        homelen = len(nums1)
        if homelen == 1 and nums1[0] == 0:
            return nums2
        elif homelen == 1:
            return nums1
        j = 0
        awaylen = len(nums2)
        # Set a 'sentinel' bit at the end to be 'infinity'
        inf = float('inf')
        nums1[awaylen] = inf
        while j < awaylen:
            if nums1[i] < nums2[j]:
                nums1[i] = nums1[i]
                i += 1
            elif nums2[j] <= nums1[i]:
                nums1.insert(i, nums2[j])
                j += 1
            else:
                print('This shouldnt happen')
        del nums1[-awaylen:] # Clear the 'pushed' zeros
        return nums1






sample = [1,0,1,1,0,0,1,0]
zero = [0]
one = [1]

somenums = [0, 12, 342, 6543, 11234, 100000]
normnums = [0, 1, 10, 100, 1000, 10000, 100000]
ninenums = [9, 99, 999, 9999 ,99999 ,999999]

simplesq = [-4, -2, -1, 0, 1, 2, 4]

emm = [1,2,3,0,0,0]
enn = [2,5,6]
edgecase = ([1], [])
weirdo = ([1,0], [2])
justone = ([0], [1])

s = Solution()
print(s.merge(emm, enn))
print(s.merge(*edgecase))
print(s.merge(*weirdo))
print(s.merge(*justone))
        
