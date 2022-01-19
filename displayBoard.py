def display_board(board):
    print('\n'*100)

    empty_cell = '\t|\t|\t'
    vertical_line = "------------------------"
    print(empty_cell)
    print('   '+board[7]+'    |   '+board[8]+'   |   '+board[9])
    print(empty_cell)
    print(vertical_line)
    print(empty_cell)
    print('   '+board[4]+'    |   '+board[5]+'   |   '+board[6])
    print(empty_cell)
    print(vertical_line)
    print(empty_cell)
    print('   '+board[1]+'    |   '+board[2]+'   |   '+board[3])
    print(empty_cell)


#test_board = ['#','X','O','X','O','X','O','X','O','X']
#display_board(test_board)
