#LESSON 13: 2D LISTS AND GRIDS
#
#A grid is a list of rows; grid[r][c] is
#row r, column c. Read the lesson first.
#Under EVERY solution write:
#  # Time: O(...)  reason
#  # Space: O(...) reason
#For grids use rows and cols as the two
#sizes: a full scan is O(rows * cols).


#=========== PART A: WARM-UPS ===========

#W1 [EASY]: grid_size(grid)
#
#Input:  grid, a list of rows (every row
#        has the same length)
#Output: a tuple (rows, cols)
#Rules:
# - an empty grid [] has 0 rows and 0 cols;
#   check it before touching grid[0]
#Examples:
# grid_size([[1, 2, 3], [4, 5, 6]]) -> (2, 3)
# grid_size([[7]])                  -> (1, 1)
# grid_size([])                     -> (0, 0)

def grid_size(grid):
    

#W2 [EASY]: sum_grid(grid)
#
#Input:  grid, a list of rows of ints
#Output: an int, the sum of every cell
#Rules:
# - nested loops; do not use sum()
#Examples:
# sum_grid([[1, 2], [3, 4]]) -> 10
# sum_grid([[5]])            -> 5
# sum_grid([])               -> 0



#W3 [EASY]: make_grid(rows, cols, value)
#
#Input:  rows, cols, ints; value, anything
#Output: a NEW grid with rows rows and cols
#        columns, every cell = value
#Rules:
# - use a comprehension (see the lesson)
# - NOT [[value] * cols] * rows (the trap)
# - test that the rows are separate:
#     g = make_grid(2, 3, 0)
#     g[0][0] = 9
#     print(g)  -> [[9, 0, 0], [0, 0, 0]]
#Examples:
# make_grid(2, 3, 0)   -> [[0, 0, 0], [0, 0, 0]]
# make_grid(1, 2, ".") -> [[".", "."]]



#=========== PART B: EXERCISES ===========

#EXERCISE 1 [EASY]: row_sums(grid)
#
#Input:  grid, a list of rows of ints
#Output: a list with the sum of each row
#Rules:
# - you MAY use sum() on one row here
#Examples:
# row_sums([[1, 2, 3], [4, 5, 6]]) -> [6, 15]
# row_sums([])                     -> []



#EXERCISE 2 [MEDIUM]: col_sums(grid)
#
#Input:  grid, a non-empty list of rows
#        of ints
#Output: a list with the sum of each COLUMN
#Rules:
# - outer loop over columns, inner loop
#   over rows (the opposite of usual)
# - no sum(), no zip
#Examples:
# col_sums([[1, 2, 3], [4, 5, 6]]) -> [5, 7, 9]
# col_sums([[7], [8]])             -> [15]



#EXERCISE 3 [MEDIUM]: find_in_grid(grid, target)
#
#Input:  grid, a list of rows; target
#Output: a tuple (r, c) of the FIRST cell
#        equal to target, scanning row by row
#        left to right; (-1, -1) if not found
#Rules:
# - stop as soon as you find it
#Examples:
# find_in_grid([[1, 2], [3, 2]], 2) -> (0, 1)
# find_in_grid([[1, 2], [3, 4]], 4) -> (1, 1)
# find_in_grid([[1, 2], [3, 4]], 9) -> (-1, -1)



#EXERCISE 4 [MEDIUM]: diagonal_sum(grid)
#
#Input:  grid, a SQUARE grid (n rows, n cols)
#Output: the sum of both diagonals:
#        top-left to bottom-right AND
#        top-right to bottom-left
#Rules:
# - ONE loop over i from 0 to n - 1
# - main diagonal cell:  grid[i][i]
# - other diagonal cell: grid[i][n - 1 - i]
# - when n is odd the middle cell is on
#   BOTH diagonals: count it only once
#Examples:
# diagonal_sum([[1, 2, 3],
#               [4, 5, 6],
#               [7, 8, 9]])  -> 25   (1+5+9 + 3+7)
# diagonal_sum([[1, 2],
#               [3, 4]])     -> 10
# diagonal_sum([[5]])        -> 5
#LeetCode 1572.



#EXERCISE 5 [MEDIUM]: transpose(grid)
#
#Input:  grid, a non-empty list of rows
#        (not always square)
#Output: a NEW grid where row r becomes
#        column r: result[c][r] = grid[r][c]
#Rules:
# - the result has cols rows and rows cols
# - start from make_grid(cols, rows, 0),
#   then fill it with nested loops
#Examples:
# transpose([[1, 2, 3],
#            [4, 5, 6]])  -> [[1, 4], [2, 5], [3, 6]]
# transpose([[7]])        -> [[7]]
#LeetCode 867.



#EXERCISE 6 [MEDIUM]: count_neighbours(grid, r, c)
#
#Input:  grid of 0s and 1s; r, c a cell
#Output: how many of the 4 neighbours
#        (up, down, left, right) are 1
#Rules:
# - use the directions list from the lesson:
#     [(-1, 0), (1, 0), (0, -1), (0, 1)]
# - skip neighbours outside the grid (bounds
#   check BEFORE reading the cell)
# - do not count the cell itself
#Examples:
# g = [[1, 1, 0],
#      [0, 1, 1],
#      [1, 0, 1]]
# count_neighbours(g, 1, 1) -> 2   (up 1, down 0, left 0, right 1)
# count_neighbours(g, 0, 0) -> 1   (only right and down exist; right is 1)
# count_neighbours(g, 2, 2) -> 1   (up is 1, left is 0)



#EXERCISE 7 [HARD]: is_valid_sudoku(board)
#
#Input:  board, a 9 x 9 grid of strings:
#        digits "1"-"9" or "." for empty
#Output: True if no digit repeats in any
#        row, any column, or any 3 x 3 box;
#        otherwise False (empty cells are fine,
#        the board does NOT have to be solvable)
#Rules:
# - ONE pass over all 81 cells
# - keep a set for every row, every column
#   and every box (27 sets in total)
# - the box of cell (r, c) is
#     (r // 3, c // 3)   (see the lesson)
# - seen-set pattern: if the digit is already
#   in its row set, col set or box set ->
#   return False; otherwise add it to all 3
#LeetCode 36 - on NeetCode 150.
#
#Test boards:

board_ok = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

#Same board, but the top-left "5" becomes "8":
#now column 0 has two 8s and the top-left
#box has two 8s.
board_bad = [row[:] for row in board_ok]
board_bad[0][0] = "8"

# is_valid_sudoku(board_ok)  -> True
# is_valid_sudoku(board_bad) -> False
