# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 


class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        opening = "({["
        closing = ")}]"
        
        for char in s:
            if char in opening:
                stack.append(char)
            elif char in closing:
                if len(stack) == 0:
                    return False
                elif closing.index(char) != opening.index(stack.pop()):
                    return False 
        
        return len(stack) == 0
    
    
    
#Runtime 38 ms Beats 54.64%
#Memory 13.9 MB Beats 21.85%