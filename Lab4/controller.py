""" Author: Prof. Alyssa
Controls the flow of the game, including key presses.
You do NOT need to update this file.
"""

import pygame
from enum import Enum

from preferences import Preferences 
from display import BoardDisplay
from game_data import GameData


class Controller:
    def __init__(self, ai_type='bfs'):
        # The state of the current game
        self.game_data = GameData(ai_type)
        # The visual board
        self.display = BoardDisplay()
        # How many cycles have passed
        self.__num_cycles = 0 

    def run(self) -> None:
        """ The main loop of the game """

        # Draw the initial state of the board
        self.display.draw_board(self.game_data)

        # Keep track of the time that's passed 
        clock = pygame.time.Clock()

        # Loop to allow the player time to start
        key_pressed = False
        while not key_pressed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_data.set_game_over()
                elif event.type == pygame.KEYDOWN:
                    key_pressed = True
            clock.tick(Preferences.SLEEP_TIME)

        # Loop until we get a game over 
        while not self.game_data.gameover:
            # Run the main behavior
            self.cycle()
            # Sleep
            clock.tick(Preferences.SLEEP_TIME)

        # Loop to allow the player time to read the gameover screen and exit
        key_pressed = False
        while not key_pressed:
            for event in pygame.event.get():
                if event.type in [pygame.QUIT, pygame.KEYDOWN]:
                    key_pressed = True
            clock.tick(Preferences.SLEEP_TIME)

    def cycle(self) -> None:
        """ The main behavior to execute at each time step """
        
        # Check for keyboard input
        for event in pygame.event.get():
            # Quit the game
            if event.type == pygame.QUIT:
                self.game_data.set_game_over()
            # Change the direction based on the keypress
            elif event.type == pygame.KEYDOWN:
                # Change directions
                if event.key in self.Keypress.LEFT.value:
                    self.game_data.set_going_west()
                elif event.key in self.Keypress.RIGHT.value:
                    self.game_data.set_going_east()
                elif event.key in self.Keypress.UP.value:
                    self.game_data.set_going_north()
                elif event.key in self.Keypress.DOWN.value:
                    self.game_data.set_going_south()
                elif event.key in self.Keypress.AI.value:
                    self.game_data.set_ai_mode()

        # Update the player
        self.update_player()
        # Update the food
        self.update_food()
        # Increment the number of cycles 
        self.__num_cycles += 1
        # Update the screen
        self.display.draw_board(self.game_data)

    def update_food(self) -> None:
        """ Add food every FOOD_ADD_RATE cycles """

        if not self.game_data.food or \
                (self.__num_cycles % Preferences.FOOD_ADD_RATE == 0 and \
                not self.game_data.at_max_food()):
            self.game_data.add_food()

    def update_player(self) -> None:
        """ Move the player every REFRESH_RATE cycles """

        if self.__num_cycles % Preferences.REFRESH_RATE == 0:
            self.game_data.move_player()


    class Keypress(Enum):
        """ Define the keyboard inputs """
        UP = pygame.K_i, pygame.K_UP       # i and up arrow key
        DOWN = pygame.K_k, pygame.K_DOWN   # k and down arrow key
        LEFT = pygame.K_j, pygame.K_LEFT   # j and left arrow key
        RIGHT = pygame.K_l, pygame.K_RIGHT # l and right arrow key
        AI = pygame.K_a,                   # a


if __name__ == "__main__":
    Controller().run()