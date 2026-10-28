# Wumpus World Problem Using Artificial Intelligence

## Overview
A Python-based graphical simulation of the classic Wumpus World problem. The application uses Tkinter to display a 4×4 grid where a player navigates an environment containing hidden hazards and gold.

## Features
- Interactive 4×4 grid interface.
- Random placement of gold, a Wumpus, and a pit.
- Player movement using directional buttons.
- Percepts including breeze, stench, and glitter.
- One-arrow shooting mechanism.
- Win and game-over conditions.
- Restart functionality for a new randomly generated world.

## Technologies Used
- Python
- Tkinter
- Random module

## Artificial Intelligence Concepts
- Intelligent-agent environment
- Environment perception
- State representation
- Grid-based navigation
- Hazard detection using percepts

**Note:** This version is a manually controlled simulation. Autonomous agent reasoning and path planning are not implemented.

## How to Run

### Prerequisites
Install Python 3. The Tkinter module must also be available.

### Steps
1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run the following command:

```bash
python wumpus_world.py
```

On some systems, use `python3` instead of `python`.

## Game Rules
- Navigate the grid using the directional buttons.
- Breeze indicates that a pit is in an adjacent cell.
- Stench indicates that the living Wumpus is in an adjacent cell.
- Glitter indicates that the gold is in the current cell.
- Shoot an arrow in a direction to attempt to kill the Wumpus.
- Reach the gold to win; entering a pit or a living Wumpus's cell ends the game.

## Future Enhancements
- Autonomous agent decision-making.
- Knowledge base and logical inference.
- Safe-cell identification and path planning.
- Visual indicators for the Wumpus, pit, and gold.
- Score tracking and performance evaluation.

## Author
Sharvari Sasane
