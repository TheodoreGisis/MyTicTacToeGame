from IPython.display import clear_output
import os

#function to print the board
def ShowBorder(my_board):

    print("\n")
    print(my_board[0]+'|'+my_board[1]+'|'+my_board[2])
    print("-----")
    print(my_board[3]+'|'+my_board[4]+'|'+my_board[5])
    print("-----")
    print(my_board[6]+'|'+my_board[7]+'|'+my_board[8])

#function that return the choise of the letter of each player
def Choise():
    player1=input("Player1 What do you want X or O?\n")
    while player1 != 'X' and player1 != 'O':
        player1=input("Invalid..only X or O \n")
    return player1

#function that returns the letter of the other player
def choise2(Choise1):
        if Choise1 == 'X':
            print("So player2 is playing with 'O'\n")
            return 'O'
        else:
            print("So player2 is playing with 'X'\n")
            return 'X'
#function of decisions
def decision(decision1,board):
        while decision1 not in ['1','2','3','4','5','6','7','8','9']:
            decision1=input("Please give me a number between 0-9\n")
        return int(decision1)

#function that declare if the game is winable
def win(board,choiseOfPlayer1):
    if board[0]==board[1] and board[1]==board[2]:
        if board[0]==choiseOfPlayer1:
            print("######Player2 win########")
            ShowBorder(Board)
            return 0
        else:
            print("######Player2 win########")
            ShowBorder(Board)
            return 0
    elif board[0]==board[3] and board[3]==board[6]:
        if board[0]==choiseOfPlayer1:
            print("######Player2 win########")
            ShowBorder(Board)
            return 0
        else:
            print("######Player2 win########")
            ShowBorder(Board)
            return 0
    elif board[3]==board[4] and board[4]==board[5]:
        if board[0]==choiseOfPlayer1:
            print("######Player2 win########")
            ShowBorder(Board)
            return 0
        else:
            print("######Player2 win########")
            ShowBorder(Board)
            return 0
    elif board[6]==board[7] and board[7]==board[8]:
        if board[0]==choiseOfPlayer1:
            print("######Player2 win########")
            ShowBorder(Board)
            return 0
        else:
            print("######Player2 win########")
            ShowBorder(Board)
            return 0
    elif board[1]==board[4] and board[4] == board[7]:
        if board[0]==choiseOfPlayer1:
            print("######Player2 win########")
            ShowBorder(Board)
            return 0
        else:
            print("######Player2 win########")
            ShowBorder(Board)
            return 0
    elif board[2]==board[5] and board[5]==board[8]:
        if board[0]==choiseOfPlayer1:
            print("######Player2 win########")
            ShowBorder(Board)
            return 0
        else:
            print("######Player2 win########")
            ShowBorder(Board)
            return 0
    elif board[0]==board[4] and board[4]==board[8]:
        if board[0]==choiseOfPlayer1:
            print("######Player2 win########")
            ShowBorder(Board)
            return 0
        else:
            print("######Player2 win########")
            ShowBorder(Board)
            return 0
    elif board[2]==board[4] and board[4]==board[6]:
        if board[0]==choiseOfPlayer1:
            print("######Player2 win########")
            ShowBorder(Board)
            return 0
        else:
            print("######Player2 win########")
            ShowBorder(Board)
            return 0
    else:
        return 1
#-----------------MAIN---------------------------------
Board=['1','2','3','4','5','6','7','8','9']
print("Welcome to TicTacToe-----ARE YOU READY?")
print("    Lets the game BEGIN")
endgame=False
counter=0;
player=1
choiseOfPlayer1=Choise()
choiseOfPlayer2=choise2(choiseOfPlayer1)

while win(Board,choiseOfPlayer1)==1 and endgame==False:
    counter=counter+1
    ShowBorder(Board)
    if player==1:
        decision1=input("Player1 where do you want to put?\n")
        Player1disision=decision(decision1,Board)-1
        player=2
        Board[Player1disision]=choiseOfPlayer1
    else:
        decision1=input("Player2 where do you want to put?\n")
        Player1disision=decision(decision1,Board)-1
        Board[Player1disision]=choiseOfPlayer2
        player=1

#if counter == 8 then the game is draw
    if counter == 8 :
        print("####Τhe Game Was a DRAW#####")
        next=input("do you want to continue? Y-N?\n")
        if next == 'Y':
            Board=['1','2','3','4','5','6','7','8','9']
            ShowBorder(Board)
            choiseOfPlayer1=Choise()
            choiseOfPlayer2=choise2(choiseOfPlayer1)
        else:
            print("######HAVE A NICE DAY#######")
            endgame=True
    if win(Board,choiseOfPlayer1)==0:
        print("####Game end#####")
        next=input("do you want to continue? Y-N?\n")
        if next == 'Y':
            Board=['1','2','3','4','5','6','7','8','9']
            ShowBorder(Board)
            choiseOfPlayer1=Choise()
            choiseOfPlayer2=choise2(choiseOfPlayer1)
            counter=0
        else:
            print("######HAVE A NICE DAY#######")
            endgame=True
