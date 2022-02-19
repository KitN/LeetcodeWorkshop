from typing import List
from itertools import combinations
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

#2 <= nums.length <= 104
#-109 <= nums[i] <= 109
#-109 <= target <= 109
#Only one valid answer exists.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Function would go here
        indices = []
        even_parity = target % 2 == 0 
        even_nums, odd_nums = [], []
        even_nums = [ n for n in nums if n % 2 == 0]
        odd_nums = [ n for n in nums if n % 2 != 0]
        if even_parity:
            for combo in combinations(even_nums, 2):
                if combo[0] + combo[1] == target:
                    indices.append(nums.index(combo[0]))
                    indices.append(nums.index(combo[1]))
                    return indices
            for combo in combinations(odd_nums, 2):
                if combo[0] + combo[1] == target:
                    indices.append(nums.index(combo[0]))
                    indices.append(nums.index(combo[1]))
                    return indices
        elif not even_parity:
            for even_n in even_nums:
                for odd_n in odd_nums:
                    if even_n + odd_n == target:
                        indices.append(nums.index(even_n))
                        indices.append(nums.index(odd_n))
                        return indices



        return indices



practice_list = [2,7,11,15]
practice_target = 9
# nums = [3,2,4] target = 6
practice_list = [3,2,4]
practice_target = 6

soln = Solution()

print(soln.twoSum(practice_list, practice_target))
