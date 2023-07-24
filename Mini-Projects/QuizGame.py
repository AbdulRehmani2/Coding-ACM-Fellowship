def calculatePercentage(score):
    result = score / 5
    result = result * 100
    return result

def wrongAnswer():
    print("Wrong Answer")
    
def rightAnswer():
    print("Right Answer")
    
def main():
    score = 0
    
    ans1 = input("What does RAM stand for : ").lower()
    if(ans1 == "random access memory"):
        rightAnswer()
        score = score + 1
    else:
        wrongAnswer()
        
    ans2 = input("What does ROM stand for : ").lower()
    if(ans2 == "read only memory"):
        rightAnswer()
        score = score + 1
    else:
        wrongAnswer()
        
    ans3 = input("What does CPU stand for : ").lower()
    if(ans3 == "central processing unit"):
        rightAnswer()
        score = score + 1
    else:
        wrongAnswer()
        
    ans4 = input("What does ALU stand for : ").lower()
    if(ans4 == "arithmetic logic unit"):
        rightAnswer()
        score = score + 1
    else:
        wrongAnswer()
        
    ans5 = input("What does GPU stand for : ").lower()
    if(ans5 == "graphics processing unit"):
        rightAnswer()
        score = score + 1
    else:
        wrongAnswer()
        
    print(f"You scored {score * 2} out of 10")
    print(f"Your percentage is {int(calculatePercentage(score))}%")
    
main()