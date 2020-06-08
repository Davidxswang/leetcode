"""
https://leetcode.com/problems/implement-queue-using-stacks/
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
Notes:

You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
"""

# time complexity: O(n) for pop, O(1) for the rest
# space complexity: O(n) for pop, O(1) for the rest
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = list()
        self.len = 0
        self.queuefront = None

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if self.len == 0:
            self.queuefront = x
        self.queue.append(x)
        self.len += 1

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        tempstack = list()
        for i in range(self.len - 1):
            tempstack.append(self.queue.pop())
        ret = self.queue.pop()
        self.len -= 1
        if self.len != 0:
            for i in range(self.len):
                if i == 0:
                    self.queuefront = tempstack.pop()
                    self.queue.append(self.queuefront)
                else:
                    self.queue.append(tempstack.pop())
        else:
            self.queuefront = None
        return ret

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.queuefront

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.len == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()