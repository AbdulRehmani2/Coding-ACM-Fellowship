name = input("Enter your name : ")
print(f"Hello {name}!, Welcome to this adventure")
print(f"You wake up in an unknown place, not knowing how you got here.")
choice = input(f"You see a two paths leading forward. Where do you choose to go (left/right) : ").lower()
if(choice == "left"):
    subchoice = input("After walking for what seems like hours, you see an old man sitting facing away from you. What do you do (approach, return) : ").lower()
    if(subchoice == "approach"):
        print("As you approach the old man, he turns toward you and see his rotton face. The zombie bites your face and rips it. You resist in futility as the old man rips your body and eats you while you are still alive. After a long agonizing hour or so, you die.")
    elif(subchoice == "return"):
        print("After walking back, you see that the way lead no where and you appear to stand where you started. In this endless loop, you starve yourself to death")
elif(choice == "right"):
    subchoice = input("After walking a few hours, you approach a river. Seeing the river reminds you of your thist. Do you (drink) or (not) : ").lower()
    if(subchoice == "drink"):
        print("As you move dip your hands in the river, a fish like monster grabs your hand and pulls you into the water, drowning you to your death.")
    elif(subchoice == "not"):
        print("As you wait a while besides the river, you see a deer approaching the river to drink water. As it drinks the water, a fish-like monster bites the deers neck and drags it into the water. You thank God that you did not try to drink water before.")
        print("You Survive")