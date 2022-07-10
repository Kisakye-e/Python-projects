print("\n\t**Welcome to the Rock Paper Scissors game!**")
print("For every round you will be prompted to enter your move.\nChoose one of the following: ")
print("* Rock\n* Paper\n* Scissors\n\nPlease enter the move as shown above\n(ALL CAPITAL LETTERS MUST REMAIN CAPITAL AND SMALL LETTERS MUST BE SMALL).\nFailure to follow the rules will lead to unexpected results/errors.\n")

import random
Num_user_wins=0
Num_comp_wins=0
Num_ties=0
moves= ["Rock", "Paper", "Scissors"]
for Round in range(1,4,1):
    print("\tROUND", Round)
    comp_move=random.choice(moves)
    user_move=input("Enter your move: \n")
    if (comp_move==moves[0]):
        print("Computer move: ",moves[0])
        if(user_move==moves[1]):
            print("Your move: ",moves[1])
            print("\tYou win!\n")
            Num_user_wins+=1
        elif(user_move==moves[2]):
            print("Your move: ",moves[2])
            print("\tYou lose!\n")
            Num_comp_wins+=1
        else:
            print("Your move: ",moves[0])
            print("\tYou tied!\n")
            Num_ties+=1

    if(comp_move==moves[1]):
        print("Computer move: ",moves[1])
        if(user_move==moves[1]):
            print("Your move: ",moves[1])
            print("\tYou tied!\n")
            Num_ties+=1
        elif(user_move==moves[2]):
            print("Your move: ",moves[2])
            print("\tYou win!\n")
            Num_user_wins+=1
        else:
            print("Your move: ",moves[0])
            print("\tYou lose!\n")
            Num_comp_wins+=1
    if(comp_move==moves[2]):
        print("Computer move: ",moves[2])
        if(user_move==moves[1]):
            print("Your move: ",moves[1])
            print("\tYou lose!\n")
            Num_comp_wins+=1
        elif(user_move==moves[2]):
            print("Your move: ",moves[2])
            print("\tYou tied!\n") 
            Num_ties+=1
        else:
            print("Your move: ",moves[0])
            print("\tYou win!\n")
            Num_user_wins+=1
if(Num_user_wins>Num_comp_wins):
    print("Number of ties=", Num_ties)
    print("Number of Computer wins=", Num_comp_wins)
    print("Number of Your wins=", Num_user_wins, "\n\tYou win!")
elif(Num_user_wins<Num_comp_wins):
    print("Number of ties=", Num_ties)
    print("Number of Computer wins=", Num_comp_wins)
    print("Number of Your wins=", Num_user_wins, "\n\tYou lose!")
else:
    print("Number of ties=", Num_ties)
    print("Number of Your wins=", Num_user_wins)
    print("Number of Computer wins=", Num_comp_wins)
    print("\tYou tied!")