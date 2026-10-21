"""
Author: Esteban Jimenez Sierra
Date last updated: 10/21/2026
Stores all the data for the Duck Collector game: the board, the player's
body, the food, the score, and the movement mode. Also has the player
movement logic and the AI mode that uses BFS (Queue) or DFS (Stack) to
find the closest duck.
"""

import random
from enum import Enum, auto

from cell import Cell
from preferences import Preferences
from search_structure import Queue, Stack

class GameData:
    def __init__(self, ai_type):
        # The current state of the board
        self.board = [[Cell(row, col) for col in range(Preferences.NUM_COLS)] 
                                 for row in range(Preferences.NUM_ROWS)]

        # Whether or not the game is over
        self.gameover = False

        # The current movement mode
        self.current_mode = self.MoveMode.GOING_EAST

        # The AI type to run
        self.ai_type = ai_type

        # A list of cells containing food
        self.food = []

        # A list of cells containing the body
        self.body = self.init_player()

        # Number of food eaten
        self.score = 0

    
    ##########################
    # Initialization methods #
    ##########################

    def init_player(self):
        """ Initialize the player cell """

        # Get the top left cell
        player = self.get_cell(0,0)
        # Convert it to the player
        player.become_player()
        # Return a list with the player cell
        return [player]


    ###################################
    # Get information about the board #
    ###################################

    def in_ai_mode(self):
        """ Returns whether or not we are in AI mode """

        return self.current_mode == self.MoveMode.AI_MODE
    
    def get_cell(self, row, col):
        """ Returns the cell at the given row and column """

        if (row >= 0 and row < Preferences.NUM_ROWS) and \
                (col >= 0 and col < Preferences.NUM_COLS):
            return self.board[row][col]
        # Implied else
        raise Exception('get_cell() tried to access cell outside of board: ({}, {})'.format(
            row, col))
    
    def get_player(self):
        """ Returns the head of the body list """

        return self.body[0]
    
    def get_tail(self):
        """ Returns the end of the body list """

        return self.body[-1]
    
    def at_max_food(self) -> bool:
        """ Check whether we can add more food """

        return len(self.food) / Preferences.NUM_CELLS > Preferences.MAX_FOOD


    ###################################
    # Set information about the board #
    ###################################

    def set_game_over(self) -> None:
        """ Turn on the game over flag """

        self.gameover = True

    def set_going_north(self) -> None:
        """ Set the mode to north """

        self.current_mode = self.MoveMode.GOING_NORTH 

    def set_going_south(self) -> None:
        """ Set the mode to south """

        self.current_mode = self.MoveMode.GOING_SOUTH 

    def set_going_east(self) -> None: 
        """ Set the mode to east """

        self.current_mode = self.MoveMode.GOING_EAST 

    def set_going_west(self) -> None:
        """ Set the mode to west """

        self.current_mode = self.MoveMode.GOING_WEST 

    def set_ai_mode(self) -> None:
        """ Set the mode to AI mode """

        self.current_mode = self.MoveMode.AI_MODE


    ##############################
    # Neighbor Retrieval Methods #
    ##############################

    def get_next_cell(self):
        """ Returns the next cell to move to based on the current direction """

        return {
            self.MoveMode.GOING_NORTH : self.get_north_neighbor(self.get_player()),
            self.MoveMode.GOING_SOUTH : self.get_south_neighbor(self.get_player()),
            self.MoveMode.GOING_WEST : self.get_west_neighbor(self.get_player()),
            self.MoveMode.GOING_EAST : self.get_east_neighbor(self.get_player())
        }.get(self.current_mode)
    
    def get_west_neighbor(self, cell: Cell) -> Cell:
        """ Returns the cell immediately to the left of the given cell. 
            If we are at the boundary, return None. """
            
        if cell.get_col() - 1 < 0:
            return None 
        else:
            return self.board[cell.get_row()][cell.get_col()-1]
        
    def get_east_neighbor(self, cell: Cell) -> Cell:
        """ Returns the cell immediately to the right of the given cell.
            If we are at the edge of the map, return None. """
        
        if cell.get_col() + 1 >= Preferences.NUM_COLS:
            return None 
        else:
            return self.board[cell.get_row()][cell.get_col()+1]
    
    def get_north_neighbor(self, cell: Cell) -> Cell:
        """ Returns the cell immediately above the given cell.
            If we are at the edge of the map, return None. """
        
        if cell.get_row() - 1 < 0:
            return None 
        else:
            return self.board[cell.get_row()-1][cell.get_col()]
        
    def get_south_neighbor(self, cell: Cell) -> Cell:
        """ Returns the cell immediately below the given cell.
            If we are at the edge of the map, return None. """
        
        if cell.get_row() + 1 >= Preferences.NUM_ROWS:
            return None 
        else:
            return self.board[cell.get_row()+1][cell.get_col()]
        
    def get_neighbors(self, center: Cell):
        """ Get all valid neighbors surrounding the center cell.
            Always returns a list in order north, south, east, west """
        
        return list(filter(lambda x: x is not None, 
                [self.get_north_neighbor(center),
                self.get_south_neighbor(center),
                self.get_east_neighbor(center),
                self.get_west_neighbor(center)]))
    
    def get_random_neighbor(self, center: Cell) -> Cell:
        """ Get a random neighbor from the given cell """

        neighbors = self.get_neighbors(center)
        return random.choice(neighbors)


    ###########################
    # Player Movement Methods #
    ###########################

    def move_player(self) -> None:
        """ Move the player to the next step based on the current
            direction or as directed by AI """
        
        if self.in_ai_mode():
            next_cell = self.get_next_cell_ai()
        else:
            next_cell = self.get_next_cell()
        # Move the snake to the next cell
        self.move_player_to_cell(next_cell)

    def move_player_left(self) -> None:
        """ Move the player one cell to the left if it is empty """

        neighbor = self.get_west_neighbor(self.player)
        if neighbor:
            self.move_player_to_cell(neighbor)
        
    def move_player_right(self) -> None:
        """ Move the player one cell to the right if it is empty """

        neighbor = self.get_east_neighbor(self.player)
        if neighbor:
            self.move_player_to_cell(neighbor)

    def move_player_up(self) -> None:
        """ Move the player one cell up if it is empty """

        neighbor = self.get_north_neighbor(self.player)
        if neighbor:
            self.move_player_to_cell(neighbor)

    def move_player_down(self) -> None:
        """ Move the player one cell down if it is empty """

        neighbor = self.get_south_neighbor(self.player)
        if neighbor:
            self.move_player_to_cell(neighbor)

    def move_player_to_cell(self, cell: Cell) -> None:
        """ Move the player to the given cell """
        
        # If the cell is a body or off the map, game over
        if not cell or cell.is_body():            
            self.set_game_over()

        # If the cell is food, move forward and grow
        elif cell.is_food():
            # The old head becomes part of the body
            self.get_player().become_body()
            # The food cell becomes the new head
            cell.become_player()
            # Add the new head to the front of the body list
            self.body.insert(0, cell)
            # The duck is collected, so take it off the food list
            self.food.remove(cell)
            # Increment the player's score
            self.score += 1
            # The tail stays where it is, so the line gets one longer

        # If the cell is empty, move forward and keep the same length
        else:
            # The old head becomes part of the body
            self.get_player().become_body()
            # The empty cell becomes the new head
            cell.become_player()
            # Add the new head to the front of the body list
            self.body.insert(0, cell)
            # Remove the tail from the end of the body list
            old_tail = self.body.pop()
            # The old tail spot is now empty
            old_tail.become_empty()


    ########################
    # Food Related Methods #
    ########################

    def add_food(self) -> None:
        """ Adds food to a open spot on the board """

        # Find a row on the board
        row = random.randrange(0, Preferences.NUM_ROWS)
        # Find a col on the board
        col = random.randrange(0, Preferences.NUM_COLS)
        # Get the cell at that location
        cell = self.get_cell(row, col)

        # If it is empty, add food
        if cell.is_empty():
            cell.become_food()
            self.food.append(cell)

    def ate_food(self, food_cell: Cell) -> None:
        """ Eat the food """

        # Change the current head to a body
        self.get_player().become_body()

        # The food becomes the new player
        food_cell.become_player()
        # Add the new cell to the body
        self.body.append(food_cell)
        # Remove the cell from the food list
        self.food.remove(food_cell)

        # Increment the player's score
        self.score += 1

    ##############
    # AI methods #
    ##############

    def get_next_cell_ai(self) -> Cell:
        """ Searches for the closest duck using BFS (Queue) or DFS (Stack)
            and returns the next cell the player should move to on the path
            to it. If no path is found, returns a random neighbor. """
        
        # Prepare all the tiles to search
        self.reset_cells_for_search()

        # Initialize a structure to hold the tiles to search
        if self.ai_type == "dfs":
            cells_to_search = Stack()
        else:
            cells_to_search = Queue()

        # Start the search from the player
        player = self.get_player()
        player.set_added_to_search_list()
        cells_to_search.add(player)

        # Keep searching until there is nothing left to check
        while not cells_to_search.is_empty():
            # Grab the next cell (Queue = oldest, Stack = newest)
            current = cells_to_search.remove()

            # Found a duck, so return the first step toward it
            if current.is_food():
                return self.get_first_cell_in_path(current)

            # Otherwise add every valid neighbor we haven't seen yet
            for neighbor in self.get_neighbors(current):
                if not neighbor.on_search_list():
                    if not neighbor.is_body():
                        # Remember where we came from (breadcrumb)
                        neighbor.set_search_parent(current)
                        neighbor.set_added_to_search_list()
                        cells_to_search.add(neighbor)

        # If we get here, no path was found
        return self.get_random_neighbor(player)
    
    def get_first_cell_in_path(self, cell) -> Cell:
        """ Starting from the food cell the search found, follows the
            search parents back toward the player and returns the cell
            right next to the player on that path (the first step). """

        current = cell
        # Walk back until the next parent would be the player
        while current.get_search_parent() is not self.get_player():
            current = current.get_search_parent()
        return current

    def reset_cells_for_search(self):
        """ Clears all the search info for each cell """
        for row in self.board:
            for cell in row:
                cell.clear_search_info()

    def print_search_path(self):
        """ A helper method for printing the path """

        out = ""
        for row in self.board:
            for cell in row:
                out += "{}\t".format(cell.parent_string())
            out += "\n"
        return out

    def __str__(self):
        """ Format the board to string form for debugging """
        
        out = ""
        for row in self.board:
            for cell in row:
                out += str(cell)
            out += "\n"
        return out

    class MoveMode(Enum):
        GOING_NORTH = auto()
        GOING_SOUTH = auto()
        GOING_EAST = auto()
        GOING_WEST = auto()
        AI_MODE = auto()
