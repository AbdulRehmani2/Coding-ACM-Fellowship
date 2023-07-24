import random;

Game = { "rock" : 1, "paper" : 2, "scissor" : 3}
Games = ["rock", "paper", "scissor"]

def CheckConditions(x, y):
    if(Game[x] == Game[y]):
        return "Draw"
    elif((Game[x] == 1 and Game[y] == 2) or (Game[x] == 2 and Game[y] == 3) or (Game[x] == 3 and Game[y] == 1)):
        return "Computer Wins"
    else:
        return "Player Wins"

    
def DisplayMove(x, y):
    print(f"You chose {x}")
    print(f"The Computer chose {y}")
    
    
def main():
    x = ""
    while(x != "exit"):
        x = input("Enter your move (Rock, Paper, Scissor) or Enter \"Exit\" to quit : ").lower()
        if(x == "exit"):
            quit()
        temp = random.randint(0, 2)
        y = Games[temp]
        DisplayMove(x, y)
        print(CheckConditions(x, y))
    
main()