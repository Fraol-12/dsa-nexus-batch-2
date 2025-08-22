class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapped = {"(":")", "{":"}", "[":"]"}

        for i in range(len(s)):  # loop through characters, not indices
            if s[i] in mapped.keys():  # if it's an opening bracket
                stack.append(s[i])
            else:  # if it's a closing bracket
                if not stack:  # nothing to match with
                    return False
                top = stack.pop()  # last opening bracket
                if mapped[top] != s[i]:  # check if matches
                    return False
        
        return not stack  # True if stack is empty
