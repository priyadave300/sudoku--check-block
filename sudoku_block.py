# Write your solution here
#here we use 2 for loops and we transverse using range from row_no to row_no+3 and col_no to col+3 
#since we need 3*3 matrix and then we access sudoku[i][j] and check condition if >0 then check if that
#element in list and then return True and False

def block_correct(sudoku: list, row_no: int, column_no: int):
    new_list =[]
    for i in range(row_no, row_no+3):
        for j in range(column_no, column_no+3):
            if sudoku[i][j] >0:
                if sudoku[i][j] not in new_list:
                    new_list.append(sudoku[i][j])
                else:
                    return False
    return True
        
    
    
if __name__ == "__main__":
    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]]
    print(block_correct(sudoku, 1, 2))