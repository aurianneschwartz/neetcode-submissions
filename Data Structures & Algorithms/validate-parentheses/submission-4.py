from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        stack.append("$")

        for char in s:
            if char == "{" or char == "(" or char == "[":
                stack.append(char)

            if char == "}" and stack:
                if stack.pop() != "{":
                    return False
            
            if char == ")" and stack:
                if stack.pop() != "(":
                    return False

            if char == "]" and stack:
                if stack.pop() != "[":
                    return False
            
        
        if stack.pop() == "$":
            return True
        return False