from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count = 0
        maxlength = len(strs[0])
        best = ""
        try: 
            while count < maxlength:
                letter = strs[0][count]
                for word in strs:
                    if word[count] == letter:
                        continue
                    else:
                        return best
                count += 1
                best = strs[0][:count]
            return best
        except IndexError:
            return best


soln = Solution()

flowers = [ "flat", "flex", "fleece"]
empty = ["", ""]
singleton = [""]
nomatch = ["a", "", "b"]
something = ["box", "boxer", "boxy"]
sticky = ["ab", "a"]

print(soln.longestCommonPrefix(something))
print(something)
print(soln.longestCommonPrefix(flowers))
print(flowers)
print(soln.longestCommonPrefix(singleton))
print(singleton)
print(soln.longestCommonPrefix(nomatch))
print(nomatch)
print(soln.longestCommonPrefix(sticky))
print(sticky)
