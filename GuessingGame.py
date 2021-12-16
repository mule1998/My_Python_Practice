s=18
j=1

while j<=9:
    i=int(input("Enter a number"))
    
    if i<s:
        print ("Number is Small")
    elif i>s:
        print("Number is greater")
    else:
        print("You Entered number correctly")
        print("You win the game! Game Over!")
    
    j=j+1
print("You took guesses",counter)
if j>9:
    print("You loose the Game!you are out of guesses")


    


    