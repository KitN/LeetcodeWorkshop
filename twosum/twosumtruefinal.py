from typing import List
from itertools import combinations

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Function would go here
        indices = []
        even_parity = target % 2 == 0 
        even_nums = [ n for n in nums if n % 2 == 0]
        odd_nums = [ n for n in nums if n % 2 != 0]
        if even_parity:
            for combo in combinations(even_nums, 2):
                if combo[0] + combo[1] == target:
                    i = nums.index(combo[0])
                    j = nums.index(combo[1], i+1)
                    indices.append(i)
                    indices.append(j)
                    return indices
            for combo in combinations(odd_nums, 2):
                if combo[0] + combo[1] == target:
                    i = nums.index(combo[0])
                    j = nums.index(combo[1], i+1)
                    indices.append(i)
                    indices.append(j)
                    return indices
        elif not even_parity:
            for even_n in even_nums:
                for odd_n in odd_nums:
                    if even_n + odd_n == target:
                        indices.append(nums.index(even_n))
                        indices.append(nums.index(odd_n))
                        return indices
        return None
