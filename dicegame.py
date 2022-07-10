import random
print("\n\nWelcome to the Dice Game!")
# the players will play 5 rounds
# option 1 represents a fair 6 sided Dice
# option 2 represents a fair 8 sided Dice
def dice():
    dice=random.randint(1,2)
    return dice
def roll(num):
    if(num==1):
        roll=random.randint(1,6)
        return roll
    else:
        roll=random.randint(1,8)
        return roll
current_round=1
total_rounds=5
player1_total=0
player2_total=0
while current_round <= total_rounds:
    dice_choice1= dice()
    player1_roll =roll(dice_choice1)
    player1_total+=player1_roll
    dice_choice2=dice()
    player2_roll =roll(dice_choice2)
    player2_total+=player2_roll
    print("\n\tROUND",current_round)
    print("Player 1 \ttotal", player1_total)
    print("Player 2 \ttotal", player2_total)
    current_round+=1
if player1_total<player2_total:
    print("\n\nPLAYER 2 WINS!")
elif player1_total>player2_total:
    print("\n\nPLAYER 1 WINS!")
else:
    print("\n\nYOU TIED!")
 
