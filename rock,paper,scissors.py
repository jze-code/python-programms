import random
while True:
    useraction=input ("enter a choice,rock,paper or scissors")
    possibleactions=["rock","paper","scissors"]
    computeraction=random.choice(possibleactions)
    print(f"you chose {useraction},computer chose {computeraction}")
    if useraction==computeraction:
        print(f"both selected{useraction},its a lie!")
    elif useraction=="rock":
        if computeraction=="scissors":
            print("rock smashes scissor,you win!")
        else:
            print("paper covers rock,you lose!!")
    elif useraction=="paper":
        if computeraction=="rock":
            print("papercovers rock,you win!")
        else:
            print("scissors cuts paper,you lose!!")
    elif useraction=="scissors":
        if computeraction=="paper":
            print("scissor cuts paper,you win!")
        else:
            print("rock smashes scissors ,you lose!!")
    playagain=input("play again?,type y or n")
    if playagain!="y":
        break