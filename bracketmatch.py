class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        else:
            stack = []
            opens = "([{"
            pairs = {"(":")", "[":"]", "{":"}", }
            for bracket in s:
                if bracket in opens:
                    stack.append(bracket)
                else:
                    try:
                        if bracket == pairs[stack[-1]]:
                            stack.pop()
                            continue
                        else:
                            return False
                    except IndexError:
                        return False
            if len(stack) == 0:
                return True
            else:
                return False

empty = ""
waiting = "(((("
oddball = "({}"
closed = ")))"
pattern = "()[]{}"
normie = "([]{})"

tests = [empty, waiting, oddball, closed, pattern, normie]
soln = Solution()

for t in tests:
    print(soln.isValid(t), t)

