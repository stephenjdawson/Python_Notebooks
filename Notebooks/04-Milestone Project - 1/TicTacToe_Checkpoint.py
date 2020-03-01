# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import collections, numpy as np, sys, copy
playerturn = 1
p1name=""
p2name=""
endgame = False
gameboard = [[" "," "," "],[" "," "," "],[" "," "," "]]


# %%
while len(p1name) < 1:
    p1name = input("Player one's name: ")


# %%
while len(p2name) < 1:
    p2name = input("Player two's name: ")


# %%
#def endgame_summation(*args), can try to do this to refactor better. 
def endgame_summation(elements, name1, name2):
    '''This function sums columns, rows, and diagonals of board matrix'''
    for n in np.nditer(elements):
        if n == 3:
            print(f"{name1} wins!")
            return True
        elif n == 27:
            print(f"{name2} wins!")
            return True


# %%
def endgame_check(checkboard, name1, name2):
    '''This function checks for a win or tie'''
    board = copy.deepcopy(checkboard)
    board = [cell for cell in board if cell]
    for row in board:
        for i in range(len(row)):
            if row[i] == "X":
                row[i] = 1
            elif row[i] == "O":
                row[i] = 9
            elif row[i] == " ":
                row[i] = 0
    board = np.asmatrix(board).astype(np.int)
    #column is axis 0, row is axis 1
    rowsum = np.sum(board, axis=0, dtype=np.int32)
    colsum = np.sum(board, axis=1, dtype=np.int32)
    diagsum = np.trace(board)
    antidiagsum = np.fliplr(board)
    antidiagsum = np.trace(antidiagsum)
    sumlist = [rowsum, colsum, diagsum, antidiagsum]
    for i in sumlist:
        if endgame_summation(i, name1, name2):
            return True
    if np.count_nonzero(board) == 9:
             print("Cats game! Meoww!!")
             return True
    return False


# %%
def move_chosen(move):
    '''This function places a move symbol'''
    move = list(move)
    if playerturn == 1:
        symbol ="X"
    else:
        symbol ="O"
    gameboard[int(move[0])-1][int(move[1])-1] = symbol
    return


# %%
def cell_check(pmove, board):
    '''This function check the existing cells to make sure you are not overwriting a move, if a move exists in that cell, return blank          string to continue while loop'''
    cell = list(pmove)
    if board[int(cell[0])-1][int(cell[1])-1] != " ":
        pmove = " "
        print("Cannot go here, please choose again.")
        return pmove
    else:
        return pmove


# %%
def input_check(move,name1,name2):
    '''this function initialized input, and makes sure it is valid'''
    while len(move) != 2:
            move = user_input(name1)
            if move == True:
                print(f"You have exited the game, thank you for playing {name1} and {name2}")
                sys.exit(0)
            move = cell_check(move, gameboard)
    return move


# %%
def user_input(player):
    '''This function takes user input to make a move'''
    test = ["0","0"]
    while int(test[0]) not in range(1,3+1):
        while int(test[1]) not in range(1,3+1):
            userinput = input(f"{player} choose a tile[in the format row:column eg.11]:")
            if len(userinput) == 2 and userinput.isnumeric():
                test = list(userinput)
            elif userinput.lower() == "exit":
                return True
            else:
                continue
    return "".join([str(a) for a in test])


# %%
#print(gameboard[0], gameboard[1], gameboard[2], sep='/n') -> may work in an IDE but not here. 
while endgame == False:
    move = "0"
    endgame = endgame_check(gameboard, p1name, p2name)
    print("   1   2   3 ")
    print(f"1  {gameboard[0][0]} | {gameboard[0][1]} | {gameboard[0][2]} ")
    print("  -----------")
    print(f"2  {gameboard[1][0]} | {gameboard[1][1]} | {gameboard[1][2]} ")
    print("  -----------")
    print(f"3  {gameboard[2][0]} | {gameboard[2][1]} | {gameboard[2][2]} ")
    if playerturn == 1 and endgame == False:
        move_chosen(input_check(move,p1name,p2name))
        playerturn = 2
    elif playerturn == 2 and endgame == False:
        move_chosen(input_check(move,p2name,p1name))
        playerturn = 1


# %%


