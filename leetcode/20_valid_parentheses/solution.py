class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left_parens = {"(", "{", "["}
        matches = {")": "(", "}":"{", "]":"["}
        for c in s:
            if c in left_parens:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                else:
                    match = stack.pop()
                    if match != matches[c]:
                        return False
        return len(stack) == 0 
