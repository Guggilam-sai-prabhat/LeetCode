class Solution(object):
    def isValid(self, s):
        stack = [] 
        for c in s: 
            if c in '([{':
                stack.append(c) 
            else: # if the character is a closing bracket
                if not stack or \
                    (c == ')' and stack[-1] != '(') or \
                    (c == '}' and stack[-1] != '{') or \
                    (c == ']' and stack[-1] != '['):
                    return False 
                stack.pop() 
        return not stack 
