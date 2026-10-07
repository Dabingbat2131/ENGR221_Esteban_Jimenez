"""
Author: Esteban Jimenez Sierra
Date last updated: 10/07/2026
Description: Stores the array of carrots to be sorted and implements three
sorting algorithms (Selection Sort, Insertion Sort, and Bubble Sort) as
generator functions, so each step can be visualized in the GUI. Also includes
a method to time how long each algorithm takes to run.
"""

import random
import time

from preferences import Preferences

class SortingAlgorithms:
    def __init__(self):
        # The algorithm to sort
        self.array = []

        # Any indices to highlight
        self.inner_idx = -1
        self.outer_idx = -1 

        # A string representing the current sorting algorithm
        self.current_alg = None

        # Store the method of the sorting algorithm being run
        self.alg_method = None
    
    def create_new_array(self, length=Preferences.NUM_ELEMENTS) -> list:
        """ Create a new array to sort """
        return [random.randint(0, Preferences.MAX_VAL) \
                      for _ in range(length)]
    
    def get_next_step(self) -> None:
        """ Updates the value of self.selected_idx whenever we reach 
            a "yield" statement in any of the below sorting algorithms. """
        
        try:
            # Treats the current sorting algorithm as an iterator
            # and sets self.selected_idx to be the next "element"
            self.outer_idx, self.inner_idx = next(self.alg_method)
        # Clear the selected_idx value when we reach the end of the method
        except StopIteration:
            self.outer_idx, self.inner_idx = -1, -1

    def restart(self, new_alg, length=Preferences.NUM_ELEMENTS) -> None:
        """ Restart the sorting process with the new algorithm. 
            Creates a new array to sort. """
        
        self.current_alg = new_alg
        self.alg_method = {
            "selection" : self.selection_sort,
            "insertion" : self.insertion_sort,
            "bubble" : self.bubble_sort
        }[self.current_alg]()
        self.array = self.create_new_array(length)
        self.outer_idx, self.inner_idx = -1, -1

    def selection_sort(self):
        """ An implementation of the Selection sorth algorithm. 
            A generator function which creates an iterator that 
            iterates through each "yielded" value. """
        
        # Number of items in the array
        n = len(self.array)

        # i marks the start of the unsorted part of the array.
        # Everything to the left of i is already sorted.
        for i in range(n):
            # Show the current position we are filling
            yield -1, i
            # Assume the first unsorted item is the smallest for now
            min_idx = i

            # Scan the rest of the unsorted part to find the true smallest
            for j in range(i + 1, n):
                # Show the current smallest (outer) and the item being checked (inner)
                yield min_idx, j

                # Found a smaller item, so remember its index
                if self.array[j] < self.array[min_idx]:
                    min_idx = j 
            
            # Swap the smallest item into position i, growing the sorted part by one
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
            # Show the two items that were just swapped
            yield i, min_idx
                

    def insertion_sort(self):
        """ An implementation of the Insertion sort algorithm.
            Sorts self.array in place by taking each item and sliding it
            left until it lands in its correct spot in the sorted part.
            A generator function which yields (outer_idx, inner_idx)
            at each step so the GUI can display it. """

        # Number of items in the array
        n = len(self.array)

        # i is the item we are about to insert into the sorted part (left side)
        for i in range(n):
            # Start at the item being inserted
            j = i
            # Show the item we are inserting
            yield i, j

            # Keep sliding the item left while the one before it is bigger
            while j > 0 and self.array[j - 1] > self.array[j]:
                # Swap the item with its left neighbor
                self.array[j], self.array[j - 1] = self.array[j - 1], self.array[j]
                # Move one spot to the left to follow the item
                j -= 1
                # Show where the item moved to
                yield i, j

    def bubble_sort(self):
        """ An implementation of the Bubble sort algorithm.
            Sorts self.array in place by repeatedly comparing neighbors and
            swapping them if they are out of order, so the biggest items
            "bubble up" to the end of the array.
            A generator function which yields (outer_idx, inner_idx)
            at each step so the GUI can display it. """

        # Number of items in the array
        n = len(self.array)

        # Each pass i locks the next biggest item into place at the end
        for i in range(n - 1):
            # Track whether any swaps happened during this pass
            swapped = False

            # Compare neighbors, skipping the last i items (already sorted)
            for j in range(n - 1 - i):
                # Show the pair of neighbors being compared
                yield j, j + 1

                # If the left one is bigger, swap them
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    swapped = True
                    # Show the pair after the swap
                    yield j, j + 1

            # No swaps means the array is already sorted, so stop early
            if not swapped:
                break

    def get_runtime(self) -> float:
        """ Returns the length of time (in seconds) that it took for 
            the function_to_run to sort a list of length list_length """

        # Get the time before running
        start_time = time.time()
        # Sort the given list
        for _ in self.alg_method:
            pass
        # Get the time after running
        end_time = time.time()
        # Return the difference
        return end_time - start_time

if __name__ == "__main__":
    s = SortingAlgorithms()
    # Time each algorithm on random lists of 100, 1,000, and 10,000 items
    for alg in ["selection", "insertion", "bubble"]:
        for size in [100, 1000, 10000]:
            s.restart(alg, size)
            print(f"{alg} sort, {size} items: {s.get_runtime():.4f} seconds")