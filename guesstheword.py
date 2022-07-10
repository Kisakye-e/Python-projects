print("\nWelcome to the Guess the word game\n")
print("Guidelines")
print("You will be required to guess the word selected by the computer using the following hints.\n-The length of the word\n-Theme of the word.")
print("If you guess the wrong letter 4 times you lose\n\nSTART")
wordBank=["europe","africa","uganda","america","blue","yellow","south","north","sunshine","rain","mango","apple"]
import random
wordChoice=random.choice(wordBank) 
wordLength=len(wordChoice)
if wordChoice==wordBank[0] or wordChoice==wordBank[1]:
    print("Hint:\nThe word has", wordLength,"letters.\nTheme:continent\n")
elif wordChoice==wordBank[2] or wordChoice==wordBank[3]:
    print("Hint:\nThe word has", wordLength,"letters.\nTheme:country\n")
elif wordChoice==wordBank[4] or wordChoice==wordBank[5]:
    print("Hint:\nThe word has", wordLength,"letters.\nTheme:colour\n")
elif wordChoice==wordBank[6] or wordChoice==wordBank[7]:
    print("Hint:\nThe word has", wordLength,"letters.\nTheme:direction\n")
elif wordChoice==wordBank[8] or wordChoice==wordBank[9]:
    print("Hint:\nThe word has", wordLength,"letters.\nTheme:weather element\n")
else:
    print("Hint:\nThe word has", wordLength,"letters.\nTheme:fruit\n")
correct_letters = ["_"] * wordLength
passes = 4
while passes>0:
    guess=input("Please guess a letter\n")
    if guess in wordChoice:
        for index in range(wordLength):
            if guess==wordChoice[index]:
                correct_letters[index]=guess
    else:
        passes -=1
    guessed_word= "".join(correct_letters)
    if guessed_word == wordChoice:
        print("".join(correct_letters))
        print("\nCongratulations, You won!")
        print("The word is", guessed_word)
        break
    if passes == 0:
       print("Sorry,You have used up all your guesses.\n You lose!")
       break
    
    print(guessed_word)












