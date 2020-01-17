#!python3

import sys, os
from sudoku.generator import *
from sudoku.solver import *



def die():
    print("usage: .\main.py [-c] [-s] <parameter>")
    print("Options and arguments (and corresponding environment variables):")
    print("-c      num    : set the quantity of sudoku-endgames generated, export the result to sudoku.txt")
    print("-s      puzzle : settle the sudoku question stored in file puzzle, export the result to sudoku.txt\n")
    sys.exit()



def main():
    if len(sys.argv) != 3:
        die()


    if sys.argv[1] == "-c":
        try:
            sum = int(sys.argv[2])
        except TypeError:
            print("Parameter type error!")
            die()

        output_file = open("./sudoku.txt", 'w')
        output_file.write(transform(generate_list_3d(sum)))
        output_file.close()

        
    elif sys.argv[1] == "-s":
        try:
            puzzle_file = open(sys.argv[2], 'r')
        except:
            print("Invalid path!")
            die()

        sudoku_solved = ''
        while(True):
            sudoku_puzzle = ''
            every_first_line = puzzle_file.readline()[0:-1]

            if every_first_line != '':
                sudoku_puzzle += every_first_line+' '
                for i in range(8):
                    sudoku_puzzle += puzzle_file.readline()[0:-1]+' '
                puzzle_file.readline()
                sudoku_solved += solve_one(sudoku_puzzle)

            else:
                output_file = open("./sudoku.txt", 'w')
                output_file.write(sudoku_solved)
                puzzle_file.close()
                sys.exit()
            

    else:
        die()


if __name__ == "__main__":
    main()