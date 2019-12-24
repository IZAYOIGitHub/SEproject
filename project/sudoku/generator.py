import itertools, sys

shift = [0, 3, 6, 1, 4, 7, 2, 5, 8]
row_iter = itertools.permutations('12345789',8)
sudoku_array = []

def generate(sum):

    num = 0
    
    try:
        sum = int(sum)
    except TypeError:
        print("Parameter type error!")
        sys.exit()

    for i_first_row in range(40320):

        sudoku = [ [] for i in range(9)]
        init_row = list(next(row_iter))
        for i in range(9):
            row = init_row.copy()
            row.insert(0, '6')
            for j in range(shift[i]):
                row.insert(0,row.pop())
            sudoku[i] = row

        row_3_6_iter = itertools.permutations(sudoku[3:6], 3)
        for i_3_6_row in range(6):

            temp_row = next(row_3_6_iter)
            for i in range(3, 6):
                sudoku[i] = temp_row[i-3]

            row_6_9_iter = itertools.permutations(sudoku[6:9], 3)
            for i_6_9_row in range(6):

                temp_row = next(row_6_9_iter)
                for i in range(6, 9):
                    sudoku[i] = temp_row[i-6]

                sudoku_array.append(sudoku.copy())
                num += 1

                if num >= sum:
                    return sudoku_array
                
                 
if __name__ == "__main__":
    generate('10000')
    