import os

import time

import random


# Initialize the game board with a 2D array

def create_board(rows, cols):

    board = [[0 for _ in range(cols)] for _ in range(rows)]

    return board


# Set the initial state of the board (custom or random)

def set_initial_state(board, custom_pattern=None):

    if custom_pattern:

        for i in range(len(custom_pattern)):

            for j in range(len(custom_pattern[0])):

                board[i][j] = custom_pattern[i][j]

    else:

        # Randomly set some cells to 1 (alive)

        for i in range(len(board)):

            for j in range(len(board[0])):

                if random.random() < 0.5:

                    board[i][j] = 1

    return board


# Count the number of alive neighbors for a cell

def count_alive_neighbors(board, i, j):

    alive_neighbors = 0

    for x in range(-1, 2):

        for y in range(-1, 2):

            if x == 0 and y == 0:

                continue

            row = (i + x) % len(board)

            col = (j + y) % len(board[0])

            alive_neighbors += board[row][col]

    return alive_neighbors


# Apply the Game of Life rules to the board

def next_generation(board):

    new_board = create_board(len(board), len(board[0]))

    for i in range(len(board)):

        for j in range(len(board[0])):

            alive_neighbors = count_alive_neighbors(board, i, j)

            if board[i][j] == 1:  # Cell is alive

                if alive_neighbors < 2 or alive_neighbors > 3:

                    new_board[i][j] = 0  # Die (underpopulation or overpopulation)

                else:

                    new_board[i][j] = 1  # Stay alive

            else:  # Cell is dead

                if alive_neighbors == 3:

                    new_board[i][j] = 1  # Become alive (reproduction)

    return new_board


# Print the board to the terminal

def print_board(board):

    os.system('clear')  # Clear the terminal screen

    for row in board:

        print(' '.join(['*' if cell else ' ' for cell in row]))


# Handle user input to set custom initial state

def set_custom_pattern(rows, cols):

    custom_pattern = [[0 for _ in range(cols)] for _ in range(rows)]

    print("Enter custom initial state (0 for dead, 1 for alive):")

    for i in range(rows):

        for j in range(cols):

            custom_pattern[i][j] = int(input(f"Cell ({i}, {j}): "))

    return custom_pattern


# Main loop with user interaction features

def game_of_life(rows, cols, generations, pause=False, custom_pattern=None):

    board = set_initial_state(create_board(rows, cols), custom_pattern)

    for gen in range(generations):

        print_board(board)

        if pause:

            input("Press Enter to continue...")

        board = next_generation(board)

        time.sleep(0.5)  # Pause for 0.5 seconds between generations


# User interface to set game parameters

def set_game_parameters():

    rows = int(input("Enter number of rows: "))

    cols = int(input("Enter number of columns: "))

    generations = int(input("Enter number of generations: "))

    pause = input("Pause between generations? (y/n): ").lower() == 'y'

    custom_pattern = None

    if input("Use custom initial state? (y/n): ").lower() == 'y':

        custom_pattern = set_custom_pattern(rows, cols)

    return rows, cols, generations, pause, custom_pattern


# Run the game

rows, cols, generations, pause, custom_pattern = set_game_parameters()

game_of_life(rows, cols, generations, pause, custom_pattern)

#Understand Output : The figures you see in the terminal are the representation of the Game of Life board. Each * character represents a live cell, and each space character represents a dead cell. The board is a 2D grid, where each cell has eight neighbors (horizontally, vertically, and diagonally adjacent cells).