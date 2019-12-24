import sys, os

def die():
    print("usage: .\sudoku.exe [-c] [-s]")
    print("Options and arguments (and corresponding environment variables):")
    print("-c      num    : set the quantity of sudoku-endgames generated, export the result to sudoku.txt")
    print("-s      puzzle : settle the sudoku question stored in file puzzle, export the result to sudoku.txt")
    sys.exit()
