""" 
Author: Prof. Alyssa
Controls the flow of the game, including key presses.
You do NOT need to update this file.
"""

import pygame
import random
from enum import Enum

from preferences import Preferences 
from boardDisplay import BoardDisplay
from gameData import GameData


class Controller:
    def __init__(self):
        # The state of the current game
        self.game_data = GameData()
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
        """ The main behavior to execute at each time step.
            Only update the board when the player moves. """
        
        # Flag to check whether the player has moved
        key_pressed = False

        # Check for keyboard input
        for event in pygame.event.get():
            # Quit the game
            if event.type == pygame.QUIT:
                self.set_game_over()
            # Change the direction based on the keypress
            elif event.type == pygame.KEYDOWN:
                key_pressed = True
                # Change directions
                if event.key in self.Keypress.LEFT.value:
                    self.game_data.move_player_left()
                elif event.key in self.Keypress.RIGHT.value:
                    self.game_data.move_player_right()
                elif event.key in self.Keypress.UP.value:
                    self.game_data.move_player_up()
                elif event.key in self.Keypress.DOWN.value:
                    self.game_data.move_player_down()
                # If we got here, the keypress was not a valid
                # direction, so change the flag back
                else:
                    key_pressed = False

        # If we moved, advance the game
        if key_pressed:
            # Update the food
            self.update_food()
            # Update the enemies
            self.update_enemies()
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

    def update_enemies(self) -> None:
        """ Move the enemies and add a new one if applicable """

        # Randomly choose a direction for the enemy to move
        for i in range(len(self.game_data.enemies)):
            {
                'left' : self.game_data.move_enemy_left,
                'right' : self.game_data.move_enemy_right,
                'up' : self.game_data.move_enemy_up,
                'down' : self.game_data.move_enemy_down
            }[random.choice(['left', 'right', 'up', 'down'])](i)
            
        # Add an enemy if there is space
        if self.__num_cycles % Preferences.ENEMY_ADD_RATE == 0 and \
                not self.game_data.at_max_enemies():
            self.game_data.add_enemy()

    class Keypress(Enum):
        """ Define the keyboard inputs """
        UP = pygame.K_i, pygame.K_UP       # i and up arrow key
        DOWN = pygame.K_k, pygame.K_DOWN   # k and down arrow key
        LEFT = pygame.K_j, pygame.K_LEFT   # j and left arrow key
        RIGHT = pygame.K_l, pygame.K_RIGHT # l and right arrow key

if __name__ == "__main__":
    Controller().run()