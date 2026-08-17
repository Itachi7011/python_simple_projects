# Python Simple Projects

**A collection of 13 small, standalone Python scripts — CLI games, data visualization, and utilities — each runnable independently.**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-blue)

---

## Table of Contents

- [Why This Project Exists](#why-this-project-exists)
- [Scripts](#scripts)
- [Screenshots](#screenshots)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running a Script](#running-a-script)
- [Environment Variables](#environment-variables)
- [Known Issues](#known-issues)
- [Testing](#testing)
- [Security](#security)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

---

## Why This Project Exists

Small, focused Python scripts are a good way to practice core language features and standard-library/common third-party tools (data structures, file I/O, `matplotlib`/`pandas`, basic algorithms) one concept at a time. This repository collects 13 such scripts, each independently runnable from the command line.

## Scripts

| Script | What it does | Dependencies beyond the standard library |
|---|---|---|
| `Create_Graph_Using_User_Input.py` | Prompts for data points and plots them as a graph. | `matplotlib` |
| `Data_Visualization.py` | Reads `covid.csv` (included) with `pandas` and visualizes it with `matplotlib`. | `pandas`, `matplotlib` |
| `Game_Of_Life.py` | A console-based implementation of Conway's Game of Life — configurable grid size, generations, and optional custom starting pattern, printed to the terminal each generation. | none |
| `Mad_Libs_Game.py` | A classic Mad Libs word-substitution game via console input. | none |
| `Markov_Chain_Simulator.py` | Simulates and visualizes a Markov chain. | `matplotlib` |
| `Number_Guessing_Game.py` | Console number-guessing game. | none |
| `Password_Generator.py` | Generates random passwords from letters/digits/punctuation via `random`/`string`. | none |
| `Quiz_Game.py` | Console multiple-choice quiz game. | none |
| `Rock_paper_scissor_game.py` | Console Rock-Paper-Scissors against the computer. | none |
| `Simple_Calculator.py` | Basic console calculator (arithmetic operations). | none |
| `Simple_Chat_Program.py` | **A rule-based, keyword-matching CLI chatbot** — matches typed input against a hardcoded `responses` dictionary (see [Naming Clarification](#naming-clarification) below). Not a networked chat client. | none |
| `Sudoku_Solver.py` | Solves a Sudoku board using backtracking (`is_valid`, `solve_sudoku`). | none |
| `To_do_list.py` | A console to-do list (add/view/delete tasks) — see [Known Issues](#known-issues) regarding persistence. | none |

## Naming Clarification

`Simple_Chat_Program.py` is named "chat program" but, verified from the code, it is a single-process console script: it reads a line via `input()`, looks it up (or matches keywords) in a hardcoded `responses` dictionary, and prints a canned reply. There is no `socket` usage, no networking, and no connection between two users — this is a rule-based chatbot, not a chat client/server. Documented here so the name doesn't imply networked functionality that isn't present.

## Screenshots

> _RECOMMENDED ADDITION — for Python CLI scripts, terminal screenshots (or short asciinema/GIF recordings) are more representative than static images. See [Visual Presentation](#visual-presentation-guide) below for exactly what to capture._

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3 |
| Data / plotting | `pandas`, `matplotlib` (only for the 3 scripts listed above) |
| Everything else | Python standard library only (`random`, `string`, `os`, `time`) |

There is no `requirements.txt` in the repository — only 3 of the 13 scripts need third-party packages (`pandas`, `matplotlib`); the rest run with a stock Python 3 installation. A `requirements.txt` covering just those two packages is a reasonable, low-effort addition (see [Roadmap](#roadmap)).

## Project Structure

```
python_simple_projects/
├── Create_Graph_Using_User_Input.py
├── Data_Visualization.py
├── Game_Of_Life.py
├── Mad_Libs_Game.py
├── Markov_Chain_Simulator.py
├── Number_Guessing_Game.py
├── Password_Generator.py
├── Quiz_Game.py
├── Rock_paper_scissor_game.py
├── Simple_Calculator.py
├── Simple_Chat_Program.py
├── Sudoku_Solver.py
├── To_do_list.py
└── covid.csv                # Dataset used by Data_Visualization.py
```

## Installation

```bash
git clone https://github.com/Itachi7011/python_simple_projects.git
cd python_simple_projects

# Only needed for Create_Graph_Using_User_Input.py, Data_Visualization.py,
# and Markov_Chain_Simulator.py:
pip install pandas matplotlib
```

## Running a Script

Each script is independent — run any one directly:

```bash
python3 Number_Guessing_Game.py
python3 Sudoku_Solver.py
python3 Data_Visualization.py   # requires covid.csv in the same directory (already included)
```

## Environment Variables

None. These are local CLI scripts with no external services, API keys, or configuration.

## Known Issues

- **No `requirements.txt`.** Three scripts need `pandas`/`matplotlib`; a visitor running `Data_Visualization.py` without reading this README first will hit an `ImportError`. RECOMMENDED ADDITION: a minimal `requirements.txt` with just those two packages.
- **`To_do_list.py` has no persistence** — tasks are held in a plain in-memory list (`self.tasks`) and are lost when the program exits; there is no file/JSON/database save-load logic.
- **`Simple_Chat_Program.py`'s name suggests networked chat but implements a local rule-based responder** — see [Naming Clarification](#naming-clarification).
- **No `if __name__ == "__main__":` guard in some scripts** (verify per-file before importing any of them as a module elsewhere) — as standalone scripts run directly, this doesn't affect normal usage, but would matter if any script were ever imported rather than run.

## Testing

No automated test suite currently exists. RECOMMENDED ADDITION: unit tests for the pure-logic pieces that don't depend on console I/O — `Sudoku_Solver.py`'s `is_valid`/`solve_sudoku`, `Game_Of_Life.py`'s `next_generation`/`count_alive_neighbors`, and `Password_Generator.py` are the most straightforward candidates, since they're testable without mocking `input()`.

## Security

These are local, offline CLI scripts with no network calls, no external API keys, and no handling of sensitive data beyond whatever a user types into the console (e.g. `Password_Generator.py` generates passwords locally and does not transmit or store them anywhere).

## Roadmap

See [`docs/development.md`](docs/development.md) for the prioritized addition list, including the `requirements.txt` and to-do-list persistence.

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## License

Released under the [MIT License](LICENSE). `covid.csv` is a dataset used only as sample data for `Data_Visualization.py` — verify its original source/license before redistributing it separately from this repository.
