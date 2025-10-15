# Settlers of Catan

A Python implementation of the classic board game Settlers of Catan with a graphical interface built using tkinter. The game features a dynamically generated hexagonal map, game logic based on official rules, and network analysis using networkx.

<img width="600" alt="settlers of catan" src="https://github.com/user-attachments/assets/b2531897-474a-4f57-820f-1a567cff5d0b" />


## Features

- Interactive tkinter-based GUI with visual board representation
- Hexagonal game board generated and analyzed using networkx
- Data handling and game state management with pandas
- Complete game mechanics following official Settlers of Catan rules

## Requirements

- Python 3.9+
- tkinter
- networkx
- pandas
- matplotlib
- geopandas
- Additional dependencies listed in requirements.txt

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd <folder-name>
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows (PowerShell):**
```bash
venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Upgrade pip

```bash
python -m pip install --upgrade pip
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Game

Once your virtual environment is activated and dependencies are installed, run:

```bash
python main.py
```

## How to Play

The game follows standard Settlers of Catan rules. Players build settlements, cities, and roads while collecting resources from hexagonal tiles. Roll the dice, trade resources, and develop your strategy to reach 10 victory points first.

## License

This project is provided as-is for educational and portfolio purposes.
