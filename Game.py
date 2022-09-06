import random # importing random module for random value generation
# Snake Water Gun or Rock Paper Scissor
def gameWin(comp, you):
    if comp==you:
        return None #if both are equal, there's a tie
    elif comp=="s": # checking all possibilties of win or lose
        if you=="w":
            return False
        elif you=="g":
            return True
    elif comp=="w":
        if you=="g":
            return False
        elif you=="s":
            return True
    elif comp=="g":
        if you=="s":
            return False
        elif you=="w":
            return True

print("Comp's turn : Snake(s) Water(w) Gun(g)")
randNo=random.randint(1,3) # generating computer's random value
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
elif randNo==3:
    comp='g'

you=input("Your's turn : Sanke(s) Water(w) Gun(g)\n")

a=gameWin(comp, you)

print("Comp chose: "+comp) #displaying the choices of individuals
print("You chose : "+you)
if a==None: #decalring the results
    print("Its a tie")
elif a==True:
    print("You win")
elif a==False:
    print("You lose")