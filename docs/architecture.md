# Architecture

## Overview

This repository is a flat collection of 13 independent Python scripts. There is no shared module, no package structure (`__init__.py`), and no build pipeline — each `.py` file is meant to be run directly with `python3 <script>.py`.

## Categories

- **Console games** (`Number_Guessing_Game.py`, `Quiz_Game.py`, `Rock_paper_scissor_game.py`, `Mad_Libs_Game.py`) — simple `input()`/`print()` loops, no external state.
- **Algorithms** (`Sudoku_Solver.py` — backtracking constraint solver; `Game_Of_Life.py` — Conway's Game of Life, printed to the console generation-by-generation).
- **Utilities** (`Password_Generator.py`, `Simple_Calculator.py`, `To_do_list.py` — see note below on persistence, `Simple_Chat_Program.py` — see [README: Naming Clarification](../README.md#naming-clarification)).
- **Data / visualization** (`Create_Graph_Using_User_Input.py`, `Data_Visualization.py`, `Markov_Chain_Simulator.py`) — the only three scripts with third-party dependencies (`pandas`, `matplotlib`).

## `To_do_list.py`

Implemented as a `ToDoList` class holding `self.tasks` as a plain Python list. `add_task()`, `view_tasks()`, and `delete_task()` all operate on this in-memory list only — there is no file write/read anywhere in the file, so state does not survive the script exiting.

## `Data_Visualization.py`

Reads the bundled `covid.csv` via `pandas.read_csv("covid.csv")` — this means the script must be run with `covid.csv` in the current working directory (which it is, by default, if you `cd` into the repo first).

## `Sudoku_Solver.py`

Standard backtracking approach: `is_valid(board, row, col, num)` checks row/column/box constraints; `solve_sudoku(board)` recursively tries values and backtracks on failure; `print_board()` and `main()` handle I/O.

## No Shared Runtime

Because there is no package structure or shared module, running or importing one script has no effect on any other — each is fully independent, which is consistent with the collection's purpose as a set of small, individually-runnable examples rather than a single application.
