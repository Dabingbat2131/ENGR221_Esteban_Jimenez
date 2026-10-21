# Lab 4: Duck Collector (BFS and DFS)

Esteban Jimenez Sierra, ENGR 221

A horse (the player) collects ducks (food). Every duck you collect joins the line behind you. Run off the map or into your own line and it's game over. In AI mode the horse finds the closest duck by itself using BFS or DFS.

## Files

| File | What it does | Modified? |
|---|---|---|
| `game_data.py` | Stores the board, player body, food, score, and movement mode. Has the movement and AI search logic. | Yes: `move_player_to_cell()`, `get_next_cell_ai()`, `get_first_cell_in_path()`, header and docstrings |
| `search_structure.py` | Custom `Queue` (FIFO, used for BFS) and `Stack` (FILO, used for DFS) | Yes: `add()`, `remove()`, `is_empty()` for both |
| `answers.txt` | Answers for 1.2, 2.2.1, and Part 3 | New |
| `cell.py` | One cell on the board | No |
| `controller.py` | Game loop and key presses | No |
| `display.py` | Draws the board with pygame | No |
| `preferences.py` | Constants (grid size, speed, colors) | No |
| `tests/structures_tests.py` | pytest tests for Stack and Queue | No |
| `images/` | Horse and duck sprites | No |

## How to run

From the `Lab4` folder:

```
pip install pygame-ce pytest
python controller.py
```

Press any key to start. Arrow keys (or i/j/k/l) move. Press `a` for AI mode.

To run AI mode with DFS instead of BFS, change the last line of `controller.py` to:

```
Controller("dfs").run()
```

(The handout says `Controller().run("dfs")`, but in this starter code the AI type goes into `Controller()`, not `run()`.)

## Tests

```
py -m pytest -v -m stack .\tests\structures_tests.py
py -m pytest -v -m queue .\tests\structures_tests.py
```

All 12 tests pass.
