# Lab 3: Sorting Algorithms

**Author:** Esteban Jimenez Sierra
**Course:** ENGR 221

Sorts carrots by length so they can be bagged, and shows every step of the sort in a pygame window. Includes Selection Sort, Insertion Sort, and Bubble Sort, plus a way to time each one.

## Files

| File | What it does | Modified? |
|---|---|---|
| `controller.py` | Runs the program loop and handles key presses | No |
| `display.py` | Draws the carrots (the array) on screen | No |
| `preferences.py` | Stores constants like window size, colors, and number of carrots | No |
| `sorting_algorithms.py` | Holds the array and the three sorting algorithms, plus a runtime timer | **Yes** |
| `answers.txt` | My answers to the lab questions | **Yes (new)** |
| `images/` | Carrot pictures used for the bars | No |

## How to run

Install pygame if you don't have it:

```
pip install pygame
```

**Visualizer:** run `python controller.py`, then use these keys:

| Key | Action |
|---|---|
| `s` | Start Selection Sort |
| `i` | Start Insertion Sort |
| `b` | Start Bubble Sort |
| Right arrow or `l` | Go one step |
| Space | Auto play on/off |
| `r` | Restart with a new random array |

**Runtimes:** run `python sorting_algorithms.py` to time all three algorithms on 100, 1,000, and 10,000 items. The 10,000 runs can take a few seconds each.
