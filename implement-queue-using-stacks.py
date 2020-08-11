#Idea 1: use one of the stacks as a temporary data structures allowing to reverse the items in the primary stack. 

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = [] 
        self.stack2 = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        
        ans = self.stack2.pop()
        
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        
        return ans
            

    def peek(self) -> int:
        """
        Get the front element.
        """
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        
        ans = self.stack2.pop()
        self.stack2.append(ans)
        
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        
        return ans

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack1

#Idea3: Use a stack for input element and a stack to output them, thus reversing the stacks only once.

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_in = [] 
        self.stack_out = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack_in.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.stack_out:
            return self.stack_out.pop()
        else:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()
            

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack_out:
            ans = self.stack_out.pop()
            self.stack_out.append(ans)
            return ans
        else:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
            ans = self.stack_out.pop()
            self.stack_out.append(ans)
            return ans
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack_in and not self.stack_out

