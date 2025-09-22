Tic-Tac-Toe (Python Console Game)
A simple Tic-Tac-Toe game implemented in Python, where a human player (X) competes against a computer AI (0). The game runs in the console and demonstrates fundamental programming concepts such as loops, conditionals, functions, and basic AI decision-making.

Features:
Interactive gameplay: Human player vs. AI.

AI opponent
- Attempts to win if possible.
- Blocks the player’s winning moves.
- Chooses corners, sides, or center strategically.
Game state detection:
- Detects wins across rows, columns, and diagonals.
- Detects ties when the board is full.
 Console-based UI: Displays the board after every move.

How to Run
Clone or download this repository.
Navigate to the project folder.
Run the script in your terminal:

bash
python tic_tac_toe.py

Follow the on-screen instructions:
- Enter a number (1–9) to place your move.
- The AI will automatically respond with its move.
- The game continues until someone wins or it’s a tie.

 Gameplay Instructions
The board positions are numbered 1–9 as follows:
- Player X always goes first.
- Enter the number corresponding to the cell where you want to place your move.
- The AI (0) will then make its move.

The game ends when:
- Either player has three in a row (win).
- All cells are filled with no winner (tie).

 AI Logic
The AI follows a simple but effective strategy:
Win if possible: If the AI can win in one move, it does so.
Block the player: If the player is about to win, the AI blocks.
Choose corners: Prefers corners if available.
Choose sides: Picks sides if corners are unavailable.
Take center: Chooses the center if available.
Fallback: Picks a random available move.

READme for LinePlot.py

Company Sales Data Visualization (Python + Pandas + Matplotlib)
This project demonstrates how to use Pandas and Matplotlib in Python to analyze and visualize company sales data. The program loads sales data from a CSV file and generates a line plot showing the company’s total profit per month.

Features
Data loading: Reads sales data from a CSV file (company_sales_data.csv) using Pandas.
Data inspection: Prints the dataset to the console for quick review.

Visualization:
- Plots total profit per month as a line chart.
- Adds titles, axis labels, and markers for clarity.
- Rotates x-axis labels for better readability.
- Interactive chart: Displays the plot in a pop-up window.

Requirements
Python 3.x
Libraries:
pandas
matplotlib
Install dependencies with:

bash
pip install pandas matplotlib

How to Run
Clone or download this repository.
Place the company_sales_data.csv file in the same directory as the script.
Run the script in your terminal:
bash
python sales_plot.py
The program will:
- Print the dataset to the console.
- Display a line chart of monthly total profit.

Example Output
The program generates a line chart similar to this:
X-axis: Month number (1–12)
Y-axis: Total profit
Line: Blue line with circular markers showing profit trend
This helps visualize how the company’s profit changes month by month.

Learning Objectives
This project is a great introduction to:
Reading CSV files with Pandas.
Accessing and plotting specific columns of data.
Customizing plots with Matplotlib (titles, labels, markers, rotations).
Combining data analysis and visualization in Python.


READme for SubPlot.py

Company Sales Data Visualization (Bathing Soap & Face Wash)
This project demonstrates how to use Pandas and Matplotlib in Python to analyze and visualize company sales data. The program loads sales data from a CSV file and generates two subplots showing monthly sales trends for Bathing Soap and Face Wash.

Features
Data loading: Reads sales data from a CSV file (company_sales_data.csv) using Pandas.
Data inspection: Prints the dataset to the console for quick review.

Visualization:
Subplot 1: Bathing Soap sales per month.
Subplot 2: Face Wash sales per month.
Each plot includes titles, axis labels, markers, and gridlines.
X-axis labels are rotated for better readability.
Interactive chart: Displays the plots in a pop-up window.

Requirements
Python 3.x
Libraries:
pandas
matplotlib
Install dependencies with:

bash
pip install pandas matplotlib

 How to Run
Clone or download this repository.
Place the company_sales_data.csv file in the same directory as the script.
Run the script in your terminal:

bash
python sales_subplots.py

The program will:
Print the dataset to the console.
Display two subplots:
Bathing Soap sales per month.
Face Wash sales per month.

The program generates two subplots:
Bathing Soap Sales Per Month
X-axis: Month number (1–12)
Y-axis: Units sold
Blue line with circular markers

Face Wash Sales Per Month
X-axis: Month number (1–12)
Y-axis: Units sold
Green line with circular markers

This helps visualize how sales of different products vary month by month.

Learning Objectives
This project is a great introduction to:
Reading CSV files with Pandas.
Extracting specific columns for analysis.
Creating subplots with Matplotlib.
Customizing plots with titles, labels, markers, grids, and rotations.
Presenting multiple product trends in a single figure.
