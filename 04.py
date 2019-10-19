"""
program that lets the user play Rock-Paper-Scissors against the computer and prints the winner


"""
from random import randint
playOptions=["Rock","Paper","Scissors"]




             
playerScores=0
ComputerScores=0
tie=0

player=False

while player == False:
    
    
    for i in range(5):
        player=input("Rock,Paper,Scissors?")
        Computer=playOptions[randint(0,2)]
        if Computer == player:
            tie=tie+1
        elif player=="Rock":
            if Computer== "Paper":
                ComputerScores=ComputerScores+1
            else:
                playerScores+=1
        elif player == "paper":
            if Computer == "Scissors":
                ComputerScores=ComputerScores+1
            else:
                playerScores=playerScores +1
        elif player=="Scissors":
            if Computer == "Rock":
                ComputerScores=ComputerScores+1
            else:
                playerScores=playerScores +1
        elif player == "":
            print("Invalid choice")

    player = False

    computer= playOptions[randint(0,2)]

    #checking the scores
    
    if ComputerScores > playerScores:
        print("Computer wins by",ComputerScores)

    elif ComputerScores < playerScores:
        print( " You win by ",playerScores)
    elif playerScores == ComputerScores:
        print( "A tie")
            
    


 
    
