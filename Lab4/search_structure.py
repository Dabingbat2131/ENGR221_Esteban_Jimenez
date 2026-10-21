"""
Author: Esteban Jimenez Sierra
Date last updated: 10/21/2026
Custom Queue and Stack classes used by the AI search in game_data.py.
The Queue is FIFO (used for BFS) and the Stack is FILO (used for DFS).
Both use the same method names so the search code works with either one.
"""

class Queue():
    def __init__(self):
        # Index 0 is the front of the queue, the end is the back
        self.items = []

    def add(self, item) -> None:
        """ "Enqueue" the item to the end of the queue """
        # New items get in line at the back
        self.items.append(item)

    def remove(self):
        """ "Dequeue" the item from the front of the queue and return it """
        # The item that was added first leaves first
        return self.items.pop(0)

    def is_empty(self) -> bool:
        """ Returns whether or not the queue is empty """
        return len(self.items) == 0


class Stack():
    def __init__(self):
        # Index 0 is the bottom of the stack, the end is the top
        self.items = []

    def add(self, item) -> None:
        """ Push an item to the top (end) of the stack """
        self.items.append(item)

    def remove(self):
        """ Pop the item from the top (end) of the stack and return it """
        # The item that was added last leaves first
        return self.items.pop()

    def is_empty(self) -> bool:
        """ Returns whether or not the stack is empty """
        return len(self.items) == 0
