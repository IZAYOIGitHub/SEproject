import sys
import numpy

sudoku_solved_array = []

def nine(data):
    nine_block = np.zeros([3,3,3,3], dtype = int)
    for i in range(3):
        for j in range(3):
            nine_block[i,j] = data[3*i:3*(i+1),3*j:3*(j+1)]
    print(nine_block)
    return nine_block

def num_set(data, nine_block):
    pick_set = {}
    for i in range(9):
        for j in range(9):
            if data[i,j] == 0:
                pick_set[str(i)+str(j)] = set(np.array(range(10))) - \
                (set(data[i,:]) | set(data[:,j]) | \
                set(nine_block[i//3,j//3].ravel()))
    return pick_set

def solve_one(data):    
    insert_step = []
    while True:
        pick_set = num_set(data, nine(data))
        if len(pick_set) == 0: break
        pick_sort = sorted(pick_set.items(), key = lambda x:len(x[1]))
        item_min = pick_sort[0]
        key = item_min[0]
        value = list(item_min[1])
        insert_step.append((key, value))
        if len(value) != 0:
            data[int(key[0]), int(key[1])] = value[0]
        else:
            insert_step.pop()
            for i in range(len(insert_step)):
                huishuo = insert_step.pop()
                key = huishuo[0]
                insert_num = huishuo[1]
                if len(insert_num) == 1:
                    data[int(key[0]), int(key[1])] = 0
                else:
                    data[int(key[0]), int(key[1])] = insert_num[1]
                    insert_step.append((key, insert_num[1:]))
                    break
    return data 


def solve(path):
    
    try:
        puzzle_file = open(path, 'r')
    except:
        print("Invalid path!")
        sys.exit()

    while True:

        sudoku_puzzle = ''
        for row_i in range(9):
            try:
                sudoku_puzzle += puzzle_file.readline()[0:-1]
                sudoku_puzzle += ' '
            except EOFError:
                break
        sudoku_puzzle = numpy.array(sudoku_puzzle.split(), dtypr = int).reshape((9,9))
        sudoku_solved = solve_one(sudoku_puzzle)
        sudoku_solved_array.append(soduku_solved.copy())

    return sudoku_solved_array
