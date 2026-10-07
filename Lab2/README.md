# Lab 2: Antarctic Survival (Pygame and Lists)

**Author:** Esteban Jimenez Sierra
**Course:** ENGR 221

A grid game made with pygame. You move the player around the board to eat as much food as you can while dodging enemies that wander around. Food shows up every 10 moves and a new enemy spawns in the bottom right corner every 50 moves. Run into an enemy (or let one catch you) and it's game over.

## Files

| File | What it does | Modified? |
|---|---|---|
| `controller.py` | Runs the game loop, reads key presses, and adds food and enemies over time | No |
| `boardDisplay.py` | Draws the board, score, and game over screen | No |
| `cell.py` | Represents one cell on the board (empty, player, food, or enemy) | No |
| `gameData.py` | Stores the game state and handles neighbors, player movement, food, and enemies | **Yes** |
| `preferences.py` | Constants like board size, colors, timing, text, and image paths | **Yes** (custom images and text) |
| `part1.txt` | My answers to the Part 1 questions | **Yes (new)** |
| `pseudocode.txt` | My pseudocode for every method I implemented | **Yes (new)** |
| `images/` | Pictures for the player, food, and enemy | **Yes** (added my own) |

## Customization (Part 4)

In `preferences.py` I swapped the images and text:

| Role | Original | Mine |
|---|---|---|
| Player | `penguin.png` | `lps_dog.png` |
| Food | `fish.png` | `apple.png` |
| Enemy | `seal.png` | `skull_trooper.png` |

The score text and game over message were updated to match.

## How to run

Install pygame-ce if you don't have it:

```
pip install pygame-ce
```

Then run:

```
python controller.py
```

Move with the arrow keys (or `i` `j` `k` `l`).
