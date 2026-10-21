# Lab 4

Esteban Jimenez Sierra, ENGR 221

Duck game. The horse collects ducks and they follow it. If you hit the wall or yourself its game over. Press a for AI mode and it finds the ducks by itself with BFS or DFS.

## Files

* game_data.py: game data and movement. I wrote move_player_to_cell, get_next_cell_ai, and get_first_cell_in_path
* search_structure.py: Queue and Stack. I wrote add, remove, and is_empty
* answers.txt: my answers
* cell.py, controller.py, display.py, preferences.py: starter code, didnt change
* tests/structures_tests.py: tests for Queue and Stack

## How to run

```
python controller.py
```

Arrow keys to move, a for AI mode.

For DFS change the last line in controller.py to `Controller("dfs").run()`

## Tests

```
py -m pytest -v .\tests\structures_tests.py
```
