#!python3

import sys, os
from sudoku.generator import *
from sudoku.solver import *



def die():
    print("usage: .\sudoku.exe [-c] [-s]")
    print("Options and arguments (and corresponding environment variables):")
    print("-c      num    : set the quantity of sudoku-endgames generated, export the result to sudoku.txt")
    print("-s      puzzle : settle the sudoku question stored in file puzzle, export the result to sudoku.txt")
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

        

    elif sys.argv[1] == "-s":

        try:
            puzzle_file = open(sys.argv[2], 'r')
        except:
            print("Invalid path!")
            sys.exit()

            while(True):
                sudoku_puzzle = ''
                sudoku_solved = ''

                for row_i in range(9):
                    try:
                        sudoku_puzzle += puzzle_file.readline()[0:-1]
                        sudoku_puzzle += ' '
                    except EOFError:
                        output_file = open("./sudoku.txt", 'w')
                        output_file.write(sudoku_solved)
                        sys.exit()

                sudoku_solved += solve_one(sudoku_puzzle)




    else:
        die()





if __name__ == "__main__":
    main()