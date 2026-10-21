"""
Author: Esteban Jimenez Sierra
Date: 10/21/2026
Queue and Stack classes for the AI search. Queue is for BFS, Stack is for DFS.
"""

# Queue = first in, first out (like a line at the taco truck)
class Queue():
    def __init__(self):
        self.items = []

    def add(self, item) -> None:
        """ Adds item to the back of the queue """
        self.items.append(item)  # get in line at the back

    def remove(self):
        """ Removes and returns the item at the front """
        return self.items.pop(0)  # whoever got here first leaves first (index 0)

    def is_empty(self) -> bool:
        """ Returns True if the queue is empty """
        return len(self.items) == 0  # nothing in it = empty


# Stack = last in, first out (like a pile of plates)
class Stack():
    def __init__(self):
        self.items = []

    def add(self, item) -> None:
        """ Adds item to the top of the stack """
        self.items.append(item)  # put it on top of the pile

    def remove(self):
        """ Removes and returns the item on top """
        return self.items.pop()  # grab the one on top (the last one added)

    def is_empty(self) -> bool:
        """ Returns True if the stack is empty """
        return len(self.items) == 0  # nothing in it = empty
