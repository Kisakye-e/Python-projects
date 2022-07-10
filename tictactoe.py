import random

print("\n\tWelcome to the Tic Tac Toe game.\n\nYou will be playing against the computer.\nYou are X and the computer is O.\nThe computer will be going first.\n\nThis is the board:\n")

board= {1: "",2:"", 3:"", 4:"", 5:"", 6:"", 7:"", 8:"", 9:""}

def displayHelper(num1):
    if board[num1] == '' :
        return num1
    else:
        return board[num1]

def displayBoard():
    print(displayHelper(1),displayHelper(4),displayHelper(7))
    print(displayHelper(2),displayHelper(5),displayHelper(8))
    print(displayHelper(3),displayHelper(6),displayHelper(9))
    print("\n")

displayBoard()

availablePos=[1,2,3,4,5,6,7,8,9]

def checkTriple(pos1, pos2, pos3):
    if board[pos1]=="O" and board[pos2]=="O" and board[pos3]=="O":
        print("Computer wins!")
        return True
    elif board[pos1]=="X" and board[pos2]=="X" and board[pos3]=="X":
        print("You win!")
        return True
    else:
        return False
        
def checkWinner():
    return checkTriple(1,4,7) or checkTriple(1,2,3) or checkTriple(2,5,8) or checkTriple(3,6,9) or checkTriple(4,5,6) or checkTriple(7,8,9) or checkTriple(1,5,9) or checkTriple(3,5,7)

while len(availablePos) > 0: 
    print("It is the computer's turn now.")
    computerMove= random.choice(availablePos)
    availablePos.remove(computerMove)
    board[computerMove] = "O"
    displayBoard()
    if checkWinner():
        break
    if len(availablePos)==0:
        print("You tied!")
        break
    userMove=int(input("Enter your move: "))
    availablePos.remove(userMove)
    board[userMove] = "X"
    displayBoard()  
    if checkWinner():
        break
    
print("\nThank you for playing the game.")
