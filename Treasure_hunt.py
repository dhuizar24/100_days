print("Welcome to Treasure Island.\nYour mission is to find the treasure.")


choice = input("You're at a cross road. Would you like to go left or right?")
lower_choice = choice.lower()



if lower_choice == "left":
    choice_2 = input("You come to a lake. There is an island in the lake. Type 'wait' to wait for a boat or 'swim' to swim across")
    if choice_2 == 'wait':
        choice_3 = input("The dev of this game has no ideas for games or puzzles, so now you have to choose one of three different colored doors. Pick 'red', 'blue', or 'yellow'")
        if choice_3 == 'red':
                print("You dead for some reason")
        elif choice_3 == 'blue':
                print('You died for some reason')
        elif choice_3 == 'yellow':
                print("yellow for some reason is the right one, congrats. you get nothing from this..... but thx for playing i guess")
    elif choice_2 == 'swim':
        print("You knew damn right you don't know how to swim yet you still tried and drowned, game over. -_-")      
elif lower_choice == "right": 
    print("Saw a monster and died for incovenience sake")
else:
    print("Please choose 'left' or 'right'")