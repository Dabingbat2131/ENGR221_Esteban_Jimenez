""" Author: Prof. Alyssa
Controls the flow of the program, including key presses.
You do NOT need to update this file.
"""

import pygame
from enum import Enum 

from display import Display
from sorting_algorithms import SortingAlgorithms
from preferences import Preferences

class Controller:
    def __init__(self):
        # The sorting algorithms
        self.sorting_algorithms = SortingAlgorithms()
        # The visual screen
        self.display = Display()
        # How many cycles have passed
        self.__num_cycles = 0 

        # Whether or not the user has quit out of the game
        self.quit = False
        # Whether or not to continuously advance
        self.continuous = False

    def run(self) -> None:
        """ The main loop """

        # Draw the initial state of the board
        self.display.draw(self.sorting_algorithms.array)

        # Keep track of the time that's passed 
        clock = pygame.time.Clock()

        # Loop until we quit
        while not self.quit:
            # Run the main behavior
            self.cycle()
            # Sleep
            clock.tick(Preferences.SLEEP_TIME)

    def cycle(self) -> None:
        """ The main behavior to execute at each time step.
            Only update when the user indicates to do so. """
        
        # Flag to check whether the player has moved
        key_pressed = False

        # Check for keyboard input
        for event in pygame.event.get():
            # Quit the game
            if event.type == pygame.QUIT:
                self.quit = True
            # Advance to the next step based on the keypress
            elif event.type == pygame.KEYDOWN:
                key_pressed = True 
                # Advance one step
                if self.sorting_algorithms.current_alg and event.key in self.Keypress.NEXT.value:
                    self.sorting_algorithms.get_next_step()
                    self.display.draw(self.sorting_algorithms.array, 
                                      self.sorting_algorithms.outer_idx,
                                      self.sorting_algorithms.inner_idx)
                    self.continuous = False 
                # Toggle continue advancing
                elif self.sorting_algorithms.current_alg and event.key in self.Keypress.CONT.value:
                    self.continuous = not self.continuous
                # Switch to Insertion Sort
                elif event.key == pygame.K_i:
                    self.sorting_algorithms.restart("insertion")
                # Switch to Selection Sort
                elif event.key == pygame.K_s:
                    self.sorting_algorithms.restart("selection")
                # Switch to Bubble Sort
                elif event.key == pygame.K_b:
                    self.sorting_algorithms.restart("bubble")
                # Reset with the current algorithm
                elif self.sorting_algorithms.current_alg and event.key == pygame.K_r:
                    self.sorting_algorithms.restart(self.sorting_algorithms.current_alg)
                # If we got here, the keypress was not valid,
                # so change the flag back
                else:
                    key_pressed = False

        # Advance to the next step even if there was no key pressed
        if self.continuous:
            self.sorting_algorithms.get_next_step()
            self.display.draw(self.sorting_algorithms.array, 
                                      self.sorting_algorithms.outer_idx,
                                      self.sorting_algorithms.inner_idx)

        # Update the screen to reflect any new input
        if key_pressed:
            self.display.draw(self.sorting_algorithms.array, 
                                      self.sorting_algorithms.outer_idx,
                                      self.sorting_algorithms.inner_idx)
            
        # Increment the number of cycles 
        self.__num_cycles += 1


    class Keypress(Enum):
        """ Define the keyboard inputs """
        NEXT = pygame.K_l, pygame.K_RIGHT  # l and right arrow key
        CONT = pygame.K_SPACE,              # space key

if __name__ == "__main__":
    Controller().run()