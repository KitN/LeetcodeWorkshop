# A class to read roman numerals as an int.
import pudb; pu.db
class Solution:
    """ A solution to a leetcode problem"""
    unique_tokens = ( 
        "MMM", "MM", "M",
        "CM", "CD",
        "DCCC", "DCC", "DC", "D", "CCC", "CC", "C",
        "XC", "XL",
        "LXXX", "LXX", "LX", "L", "XXX", "XX", "X",
        "IX", "IV",
        "VIII", "VII", "VI", "V", "III", "II", "I")
    unique_values = (
        3000, 2000, 1000,
        900, 400,
        800, 700, 600, 500, 300, 200, 100,
        90, 40,
        80, 70, 60, 50, 30, 20, 10,
        9, 4,
        8, 7, 6, 5, 3, 2, 1)
    unique_dict = dict(zip(unique_tokens, unique_values))

    def romanToInt(self, s: str) -> int:
        decimal_sum = 0
        for token in self.unique_dict:
            if s.startswith(token):
                # Cut the token of the start
                s = s.replace(token, "", 1)
                # Add the value to the sum
                decimal_sum += self.unique_dict[token]
        return decimal_sum

converter = Solution()

someromans = [
        "MCMXCIV"]

for roman in someromans:
    print(converter.romanToInt(roman))
