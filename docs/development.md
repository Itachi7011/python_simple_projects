# Development Guide

## Prerequisites

Python 3.x. `pandas` and `matplotlib` are only needed for `Create_Graph_Using_User_Input.py`, `Data_Visualization.py`, and `Markov_Chain_Simulator.py`.

## Running Locally

```bash
git clone https://github.com/Itachi7011/python_simple_projects.git
cd python_simple_projects
pip install pandas matplotlib   # only if running one of the 3 data/plotting scripts

python3 Number_Guessing_Game.py
```

## Suggested Next Steps

In rough priority order:

1. **Add a `requirements.txt`** with `pandas` and `matplotlib`, so `pip install -r requirements.txt` covers the three scripts that need them.
2. **Add persistence to `To_do_list.py`** — a JSON file (`tasks.json`) written/read on each add/delete/exit would be a minimal, self-contained way to fix the "tasks vanish on exit" issue documented in the README.
3. **Add unit tests** for the pure-logic functions that don't require mocking `input()`: `Sudoku_Solver.is_valid`/`solve_sudoku`, `Game_Of_Life.count_alive_neighbors`/`next_generation`, `Password_Generator`'s character-set logic.
4. **Consider clarifying `Simple_Chat_Program.py`'s name** (e.g. to `Simple_Chatbot.py`) or leave the name and rely on the README's clarification — either is fine, but pick one deliberately.

## Project Conventions

- **One script, one file, no shared imports between scripts.** Keep new scripts consistent with this pattern unless you're deliberately introducing shared code (in which case, restructure into a proper package with `__init__.py` and update this doc).
- **Console I/O via `input()`/`print()`** is the standard interface for the games/utilities; the 3 data-visualization scripts additionally open a `matplotlib` window.

## Before Opening a Pull Request

- Run the script directly (`python3 <script>.py`) to confirm it works end-to-end, including any prompts.
- If your script needs a new third-party package, add it to `requirements.txt` (once it exists) and document it in the README's Scripts table.
