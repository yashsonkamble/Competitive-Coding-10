"""
I saved the next element during initialization so that peek() can return it without moving the iterator. In next(), I return the saved value and then update it by calling the underlying iterator. This way, peek() always gives the upcoming value and hasNext() checks if it's not None.
Time Complexity: O(1)
Space Complexity: O(1)
"""
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.nextElement = self.iterator.next() if self.iterator.hasNext() else None
         
    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.nextElement
        

    def next(self):
        """
        :rtype: int
        """
        current = self.nextElement
        self.nextElement = self.iterator.next() if self.iterator.hasNext() else None
        return current
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.nextElement is not None
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].