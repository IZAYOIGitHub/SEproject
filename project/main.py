import sys, os
import gadget, sudoku_generator, sudoku_solver

def main(){

    if len(sys.argv) != 3:
        die()
    if sys.argv[1] == "-c":
        generate(sys.argv[2])
    elif sys.argv[1] == "-s":
        solve(sys.argv[2])
    else:
        die()

}

if __name__ == "__main__":
    main()