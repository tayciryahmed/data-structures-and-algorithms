class isValid(object):
        
    def my_solution(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opening = ['(','[','{']
        closing = [')',']','}']
        waiting_for = []
        
        if len(s) == 0 : return True 
        if len(s) == 1 : return False 
        if s[0] in closing: return False 
        if s[-1] in opening : return False
        if len(s)%2 == 1 : return False
        
        for c in s:
            if c in opening :
                waiting_for.append(closing [opening.index (c)])
            else:
                if c == waiting_for[-1]:
                    del waiting_for[-1]
                else:
                    return False
        
        if len(waiting_for) == 0: return True 
        else: return False 

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {')':'(', ']':'[', '}':'{'}
        stack = []
        
        for char in s:
            if char in mapping :
                top_element = stack.pop() if stack else '#'
                
                if top_element != mapping[char]:
                    return False

            else:
                stack.append(char)
        
        return not stack
