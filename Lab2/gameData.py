"""
Author: Esteban Jimenez Sierra
Date last updated: 10/07/2026
Description: Stores all the data for the current state of the Antarctic
Survival game, including the board, and where the player, food, and enemies
are. Handles finding neighboring cells, moving the player, adding and eating
food, and adding and moving enemies.
"""

import random

from cell import Cell
from preferences import Preferences

class GameData:
    def __init__(self):
        # The current state of the board
        self.board = [[Cell(row, col) for col in range(Preferences.NUM_COLS)] 
                                      for row in range(Preferences.NUM_ROWS)]
        
        # Whether or not the game is over
        self.gameover = False

        # The current cell containing the player
        self.player = self.board[0][0]    # Start at the top left
        self.player.become_player()

        # The number of empty cells on the board, accounting for the player cell
        self.num_empty_cells = Preferences.NUM_CELLS - 1

        # A list of cells containing food
        self.food = []
        # Number of food eaten
        self.score = 0

        # A list of cells containing enemies
        self.enemies = []


    #######################
    # Game Limits Methods #
    #######################

    def at_max_food(self) -> bool:
        """ Check whether we can add more food """
        return len(self.food) / self.num_empty_cells > Preferences.MAX_FOOD
    
    def at_max_enemies(self) -> bool:
        """ Check whether we can add more enemies """
        return len(self.enemies) / self.num_empty_cells > Preferences.MAX_ENEMIES

    def set_game_over(self) -> None:
        """ Turn on the game over flag """
        self.gameover = True


    ##############################
    # Neighbor Retrieval Methods #
    ##############################

    def get_west_neighbor(self, cell: Cell) -> Cell:
        """ Returns the cell immediately to the left of the given cell. 
            If we are at the  edge of the map, return None. """
        row = cell.get_row()
        col = cell.get_col()
        # Already in the leftmost column, so nothing to the left
        if col == 0:
            return None
        # Same row, one column to the left
        return self.board[row][col - 1]
        
    def get_east_neighbor(self, cell: Cell) -> Cell:
        """ Returns the cell immediately to the right of the given cell.
            If we are at the edge of the map, return None. """
        row = cell.get_row()
        col = cell.get_col()
        # Already in the rightmost column, so nothing to the right
        if col == Preferences.NUM_COLS - 1:
            return None
        # Same row, one column to the right
        return self.board[row][col + 1]
    
    def get_north_neighbor(self, cell: Cell) -> Cell:
        """ Returns the cell immediately above the given cell.
            If we are at the edge of the map, return None. """
        row = cell.get_row()
        col = cell.get_col()
        # Already in the top row, so nothing above
        if row == 0:
            return None
        # Same column, one row up
        return self.board[row - 1][col]
        
    def get_south_neighbor(self, cell: Cell) -> Cell:
        """ Returns the cell immediately below the given cell.
            If we are at the edge of the map, return None. """
        row = cell.get_row()
        col = cell.get_col()
        # Already in the bottom row, so nothing below
        if row == Preferences.NUM_ROWS - 1:
            return None
        # Same column, one row down
        return self.board[row + 1][col]


    ###########################
    # Player Movement Methods #
    ###########################
        
    def move_player_right(self) -> None:
        """ Move the player one cell to the right if there is a cell there """
        new_cell = self.get_east_neighbor(self.player)
        # Only move if we are not at the edge of the board
        if new_cell is not None:
            self.move_player_to_cell(new_cell)

    def move_player_left(self) -> None:
        """ Move the player one cell to the left if there is a cell there """
        new_cell = self.get_west_neighbor(self.player)
        # Only move if we are not at the edge of the board
        if new_cell is not None:
            self.move_player_to_cell(new_cell)

    def move_player_up(self) -> None:
        """ Move the player one cell up if there is a cell there """
        new_cell = self.get_north_neighbor(self.player)
        # Only move if we are not at the edge of the board
        if new_cell is not None:
            self.move_player_to_cell(new_cell)

    def move_player_down(self) -> None:
        """ Move the player one cell down if there is a cell there """
        new_cell = self.get_south_neighbor(self.player)
        # Only move if we are not at the edge of the board
        if new_cell is not None:
            self.move_player_to_cell(new_cell)

    def move_player_to_cell(self, cell: Cell) -> None:
        """ Move the player to the given cell """

        # If there is food in this cell, eat it
        if cell.is_food():
            self.eat_food(cell)
            self.update_player_cell(cell)
        # If there is an enemy in this cell, game over!
        elif cell.is_enemy():
            self.player.become_empty()
            self.set_game_over()
        # Otherwise, update the player location
        else:
            self.update_player_cell(cell)

    def update_player_cell(self, new_cell: Cell) -> None:
        """ Move the player to the new cell """
    
        # Empty the cell the player just moved away from
        self.player.become_empty()
        # Update the player to the new cell
        self.player = new_cell
        # Change the new cell to be the player type
        self.player.become_player()


    ########################
    # Food Related Methods #
    ########################

    def add_food(self) -> None:
        """ Adds food to a random open spot on the board.
            If the random spot is not empty, no food is added this time. """

        # Find a row on the board
        row = random.randrange(0, Preferences.NUM_ROWS)
        # Find a col on the board
        col = random.randrange(0, Preferences.NUM_COLS)

        cell = self.board[row][col]
        # Only put food in an empty cell (not on the player, food, or an enemy)
        if cell.is_empty():
            cell.become_food()
            # Keep track of the new food cell
            self.food.append(cell)
            # One less empty cell on the board
            self.num_empty_cells -= 1

    def eat_food(self, cell: Cell) -> None:
        """ Behavior for when the player eats food.
            Removes the food from the food list and increases the score. """
        # The food is gone, so stop tracking it
        self.food.remove(cell)
        # The player ate one more food
        self.score += 1
        # The player moves into the food cell and leaves its old cell empty,
        # so there is one more empty cell than before
        self.num_empty_cells += 1


    ##########################
    # Enemy Movement Methods #
    ##########################

    def add_enemy(self) -> None:
        """ Adds an enemy to the bottom right corner of the board.
            If the player is there, the game is over. If food is there,
            the enemy replaces it. If an enemy is already there, nothing
            happens. """
        cell = self.board[Preferences.NUM_ROWS - 1][Preferences.NUM_COLS - 1]

        # Already an enemy in the corner, so don't stack another one
        if cell.is_enemy():
            return

        if cell.is_player():
            # The enemy spawned on the player, so the player gets eaten
            self.set_game_over()
        elif cell.is_food():
            # The enemy takes the food's spot (the cell was not empty
            # before and is not empty after, so num_empty_cells stays the same)
            self.food.remove(cell)
        else:
            # The cell was empty, so now there is one less empty cell
            self.num_empty_cells -= 1

        cell.become_enemy()
        # Keep track of the new enemy
        self.enemies.append(cell)

    def move_enemy_to_cell(self, enemy_cell: Cell, 
                           cell: Cell, idx: int) -> None:
        """ Moves the enemy cell to a new location.
            idx refpresents the index of that enemy in
             the enemies list. Enemies can't move onto other enemies.
             If an enemy moves onto the player, the game is over. If it
             moves onto food, the food is destroyed. """

        # Enemies can't share a cell, so stay put
        if cell.is_enemy():
            return

        if cell.is_player():
            # The enemy caught the player
            self.set_game_over()
        elif cell.is_food():
            # The enemy squashes the food. The old enemy cell becomes empty,
            # so there is one more empty cell than before
            self.food.remove(cell)
            self.num_empty_cells += 1
        # If the cell was empty, the number of empty cells stays the same

        # Empty the cell the enemy left and move it to the new cell
        enemy_cell.become_empty()
        cell.become_enemy()
        # Update where this enemy is in the enemies list
        self.enemies[idx] = cell

    def move_enemy_left(self, idx: int) -> None:
        """ Move the enemy at index idx left one cell """
        enemy_cell = self.enemies[idx]
        new_cell = self.get_west_neighbor(enemy_cell)
        # Only move if we are not at the edge of the board
        if new_cell is not None:
            self.move_enemy_to_cell(enemy_cell, new_cell, idx)

    def move_enemy_right(self, idx: int) -> None:
        """ Move the enemy at index idx right one cell """
        enemy_cell = self.enemies[idx]
        new_cell = self.get_east_neighbor(enemy_cell)
        # Only move if we are not at the edge of the board
        if new_cell is not None:
            self.move_enemy_to_cell(enemy_cell, new_cell, idx)

    def move_enemy_up(self, idx: int) -> None:
        """ Move the enemy at index idx up one cell """
        enemy_cell = self.enemies[idx]
        new_cell = self.get_north_neighbor(enemy_cell)
        # Only move if we are not at the edge of the board
        if new_cell is not None:
            self.move_enemy_to_cell(enemy_cell, new_cell, idx)

    def move_enemy_down(self, idx: int) -> None:
        """ Move the enemy at index idx down one cell """
        enemy_cell = self.enemies[idx]
        new_cell = self.get_south_neighbor(enemy_cell)
        # Only move if we are not at the edge of the board
        if new_cell is not None:
            self.move_enemy_to_cell(enemy_cell, new_cell, idx)



if __name__ == "__main__":
    gd = GameData()
    # You can modify the line below for testing!
    print(gd.get_west_neighbor(gd.player))
    print(gd.get_east_neighbor(gd.player))
    print(gd.get_south_neighbor(gd.player))
