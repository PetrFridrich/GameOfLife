# Game of Life

This project is a Python implementation of Conway's Game of Life, a cellular automaton where cells evolve based on simple rules, creating complex patterns over time. For more information visit [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).

## Features

- Implements Conway's Game of Life with customizable grid size.
- Visualizes cell states and pattern evolution over time.
- Allows users to start, pause, and reset the game.

## Installation

**Prerequisite:** Ensure [Poetry](https://python-poetry.org/docs/#installation) is installed on your system.

1. Clone the repository:
   ```bash
   git clone https://github.com/PetrFridrich/GameOfLife.git
   ```
2.  Navigate to the project directory:
    ```bash
    cd GameOfLife
    ```
3. Install the dependencies with Poetry:
    ```bash 
    poetry install
    ```
This will install all required dependencies as defined in pyproject.toml.

## Project Structure

The project is organized as follows:

<pre>
GameOfLife/
├── src/                            # Folder with source codes
│   ├── __main__.py                 # Main script to run Game of Life
│   ├── game_of_life.py             # Core implementation of Game of Life
|   └── pygame_visualization.py     # Visualization with pygame.
├── .gitignore                      # Git ignore file
├── pyproject.toml                  # Poetry configuration and dependencies
├── poetry.lock                     # Poetry lock file to ensure consistent dependencies
├── LICENSE                         # License file for the project
└── README.md                       # This README file
</pre>

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.