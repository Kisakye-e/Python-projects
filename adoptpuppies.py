
import random
class Puppy():
    def __init__(self, name,age,size,breed):
        self.name = name
        self.age = age 
        self.size = size
        self.breed = breed
    def bark(self,userName):
        print("\n"+self.name+" is barking")
        print(self.name,"wants to play with you",userName,"\n")    
    def play(self):
        print("\n"+self.name,"is playing with you\n")
    def wag(self):
        print(self.name,"is wagging\n") 
    def smile(self):
       print(self.name,"is smiling\n")
    def whimper(self):
        print("\n"+self.name,"is whimpering.\nWould you like to play with",self.name,"?")      
print("\nHi there, welcome to the Adopt Puppies Program.")
userName=input("\nPlease enter your name: ")
print("\nNice to meet you",userName,"!")
numPuppies=int(input("\nHow many puppies would you like to adopt today? : "))
print(numPuppies,"it is.")
puppies=[]
print("\nNow I'll ask you to provide information on each puppy you would like to adopt")

def puppyInformation(numPuppies):
  for i in range(1, numPuppies + 1):
     print("\n\tPuppy",i)
     name=input("What is the name of the puppy? : ")
     age=int(input("How old(in weeks) is the puppy? : "))
     size=input("What is the size of the puppy?(Choose from Small,Medium,Large) : ")
     breed=input("What is the breed of the puppy? : ")
     puppy=Puppy(name,age,size,breed)
     puppies.append(puppy)
  for i in range(1,len(puppies)+1):
     print("\n\tSummary of puppy #",i,"information.")
     print("Name: ",puppies[i-1].name)
     print("Age in weeks:",puppies[i-1].age)
     print("Size: ",puppies[i-1].size)
     print("Breed: ",puppies[i-1].breed)
puppyInformation(numPuppies)
confirm=input("\nConfirm if the above information is correct - Please enter yes or no in all lowercase: ")
while confirm == "no":
    puppies.clear()
    puppyInformation(numPuppies)
    confirm2=input("Confirm if the above information is correct - Please enter yes or no in all lowercase: ")
    if confirm2 == "yes":
         break
print("\nThank you for using our service.")
onePuppy=random.choice(puppies)
onePuppy.bark(userName)
print("Will you play with",onePuppy.name,"?")
reply=input("Please enter yes or no in all lowercase : ")
while reply == "no":
  onePuppy.whimper()
  reply2=input("Please enter yes or no all in lowercase: ")
  if reply2 == "yes":
     break
onePuppy.play()
onePuppy.wag()
onePuppy.smile()