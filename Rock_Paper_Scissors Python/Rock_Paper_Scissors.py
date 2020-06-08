import time
print("Made by Sagar B Patel ")
loose = {"The computer Wins"}
win = {"You Win"}
lives = 5
score = 0
drew = 0
computer_lives = 7
while True:
    password_list=[]
    print("To begin fill in the below information...")
    username = input("Please Enter your username:  ")
    password = input("Please Enter your password:  ")
    searchfile = open("accounts.txt","r")
    for line in searchfile:
        password_list.append(line.strip())
        if username in password_list and password in password_list:
            print("Access Granted....")
            time.sleep(0.5)
            print("Loading....")
            time.sleep(0.5)
            print("Loading....")
            time.sleep(0.5)
            print("Access Granted....")
            print("-----------ROCK PAPER SCISSORS-----------")
            print("----------------Live Rules---------------")
            print("You start with ",lives, " lives")
            print("If you win you will get score increased")
            print("If you loose, you will loose a live")
            print("If you draw, the lives stay same")
            print("-----------------------------------------")
            print("To see a list of rules, type 'rules'")            
            print("-----------------------------------------")
            print("To see a list of lives, score ,drew")
            print("Type display lives/score/drew")
            print("-----------------------------------------")
            print("The computer have lives as well....")
            print("Can you beat the computer?")
            print("Good Luck....")
            print("-----------------------------------------")
            while True:
                rps = input("Rock, Paper, Scisssors?:  ")
                rps=rps.lower()
                import random
                computer=("rock","paper","scissors")
                computer=random.choice(computer)
                #rock if 
                if rps == "rock" and computer =="paper":
                    print("The Computer chose ",computer)
                    print(" ")
                    print(loose)
                    print("")
                    print("")
                    lives-=1
                if rps == "rock" and computer =="scissors":
                    print("The Computer chose ",computer)
                    print(" ")
                    print(win)
                    print("")
                    print("")
                    score+=1
                    computer_lives-=1
                #paper if statements
                if rps == "paper" and computer =="rock":
                    print("The Computer chose ",computer)
                    print(" ")
                    print(win)
                    print("")
                    print("")
                    computer_lives-=1
                    score+=1
                if rps == "paper" and computer =="scissors":
                    print("The Computer chose ",computer)
                    print(" ")
                    print(loose)
                    print("")
                    print("")
                    lives-=1                    
                #scissor if statements
                if rps == "scissors" and computer =="paper":
                    print("The Computer chose ",computer)
                    print(" ")
                    print(win)
                    print("")
                    print("")
                    computer_lives-=1
                    score+=1
                if rps == "scissors" and computer =="rock":
                    print("The Computer chose ",computer)
                    print(" ")
                    print(loose)
                    print("")
                    print("")
                    lives-=1
                if rps != "scissors" and rps != "rock" and rps != "paper":
                    print("Incorrect type...")
                #duplicates
                if rps == "rock" and computer =="rock":
                    print("The Computer chose ",computer)
                    print(" ")
                    print("You Drew")
                    print("")
                    print("")
                    drew+=1                
                if rps == "paper" and computer =="paper":
                    print("The Computer chose ",computer)
                    print(" ")
                    print("You Drew")
                    print("")
                    print("")
                    drew+=1                
                if rps == "scissors" and computer =="scissors":
                    print("The Computer chose ",computer)
                    print(" ")
                    print("You Drew")
                    print("")
                    print("")
                    drew+=1
                #system
                if rps=="rules":
                    print("---------------------------")
                    print("-----------Rules-----------")
                    print("---------------------------")
                    print("Rock beats Scissors")
                    print("Rock looses against Paper")
                    print("Paper beats Rock")
                    print("Paper looses against Scissors")
                    print("Scissors beats Paper")
                    print("Scissors losses against Rock")
                if rps=="display lives":
                    print("Lives: ",lives)
                if rps=="display score":
                    print("Score: ",score)
                if rps=="display drew":
                    print("Drew: ",drew)
                #lives
                if lives ==0 or rps =="test":
                    print("Thanks for playing..")
                    print("You have ran out of lives")
                    print("You got ",score," wins")
                    print("You drew ",drew," times")
                    stop=input("Press enter to exit")
                    exit()
                if computer_lives ==0:
                    print("Thanks for playing..")
                    print("Computer lost all it's lives. You Win !!!")
                    print("You got ",score," wins")
                    print("You drew ",drew," times")
                    stop=input("Press enter to exit")
                    exit()
                #exit
                if rps=="exit":
                    break
        else:
            print("Your username or password is incorrect..")
            print("-----------------------------------------")
            
               
            
                                       
