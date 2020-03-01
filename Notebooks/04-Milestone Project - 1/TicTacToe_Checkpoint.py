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
def endgame_summation(elements):
    #for n in elements:
        for n in np.nditer(elements):
            if n == 3:
                print("X wins!")
                return True
            elif n == 27:
                print("O wins!")
                return True


# %%
def endgame_check(checkboard, name1, name2):
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
    #sumlist = [rowsum, colsum, diagsum, antidiagsum]
    #REFACTOR BELOW, can make into a single function call? 
    #endgame_summation(sumlist)
    endgame_summation(rowsum)
    endgame_summation(colsum)
    endgame_summation(diagsum)
    endgame_summation(antidiagsum)
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
def user_input(player):
    '''This function takes user input to make a move'''
    test = ["0","0"]
   # try:
    while int(test[0]) not in range(1,3+1):
        while int(test[1]) not in range(1,3+1):
            userinput = input(f"{player} choose a tile[in the format row:column eg.11]:")
            if len(userinput) == 2:
                test = list(userinput)
                continue
            elif userinput.lower() == "exit":
                return True
            else:
                continue
    return "".join([str(a) for a in test])
  #  except ValueError:
   #     print("Oops!  That was no valid number.  Try again...")


# %%
# print(gameboard[0], gameboard[1], gameboard[2], sep='/n') -> may work in an IDE but not here. 
while endgame == False:
    move = "0"
    move2 = "0"
    endgame = endgame_check(gameboard, p1name, p2name)
    print("   1   2   3 ")
    print(f"1  {gameboard[0][0]} | {gameboard[0][1]} | {gameboard[0][2]} ")
    print("  -----------")
    print(f"2  {gameboard[1][0]} | {gameboard[1][1]} | {gameboard[1][2]} ")
    print("  -----------")
    print(f"3  {gameboard[2][0]} | {gameboard[2][1]} | {gameboard[2][2]} ")
    #Refactor this section to be ONE While loop (maybe break while out as a function).
    if playerturn == 1 and endgame == False:
        while len(move) != 2:
            move = user_input(p1name)
            if move == True:
                print(f"You have exited the game, thank you for playing {p1name} and {p2name}")
                sys.exit(0)
            move = cell_check(move, gameboard)
        move_chosen(move)
        playerturn = 2
        continue
    elif playerturn == 2 and endgame == False:
        while len(move2) != 2:
            move2 = user_input(p2name)
            if move2 == True:
                print(f"You have exited the game, thank you for playing {p1name} and {p2name}")
                sys.exit(0)
            move2 = cell_check(move2, gameboard)
        move_chosen(move2)
        playerturn = 1
        continue       
        

