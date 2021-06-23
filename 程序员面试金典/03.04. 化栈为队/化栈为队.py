class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.A = list()
        self.B = list()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.A.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.B:
            return self.B.pop()

        if self.A:
            while self.A:
                self.B.append(self.A.pop())
            return self.B.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.B:
            return self.B[-1]

        if self.A:
            while self.A:
                self.B.append(self.A.pop())
            return self.B[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if not self.B and not self.A:
            return True
        return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
