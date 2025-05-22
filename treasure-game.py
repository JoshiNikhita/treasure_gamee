print("welcome to treasure island")
print("Your fate depends on your gut feeling...")
print("Your mission is to find the treasure.")
print("You are at a cross road where do you want to go?")
choice1= input('\n\ttype "left" or "right  "').lower()
if choice1 == "left":
    print("you have come to a lake. there is an island in the middle of lake")
    choice2= input('\n\ttype "swim" or "wait  "')
    if choice2 == "wait":
        print("you arrive at the island unharmed.now there are two door pink,red,gold.") 
        choice3= input("\n\tpick one door  ")
        if choice3 == "pink":
            print("congrats, you won!")
        elif choice3 == "red":
            print("You’re bitten! Snakes behind the red door! game over.")
        else:
            print("A hidden trap shoots arrows at you! game over.")
    else:
        print("Attacked beneath the waves! game over.")
else:
    print("You walk right and trigger a hidden trap! game over.")
print("hope you enjoyed this game! play again")

    

        

    
          
          