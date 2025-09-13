#Jose Builes Lemus and Emanuel Gaviria.

#Variable to get the name of the player.
player = input("Enter Your Name for the Quest: ")
print(f'Hi {player}, you are locked in a maze. To get out, you have to correctly answer our riddles.'
      f' Good luck!')

#Getting variables of puzzles ready to run the code easily.

puzz1 = 'The more you take, the more you leave behind. What am I?'
puzz2 = 'I am an odd number. Take away a letter, and I become even. What am I?'
puzz3 = 'I have cities but no houses, forests but no trees, and rivers but no water. What am I?'
puzz4 = "David's father has three sons: Snap, Crackle and:"
puzz5 = "What is your name?: "


#Entering in room 1.
currRoom = 1

# Creating the while loop to make the player explore while they are into the game.
while currRoom != 6:  # We decided to put != 6 because if we do != 5, the code will exit the game earlier.
    #Creating outcome when entering in room 1.
    if currRoom == 1:
        answ1 = input(f"Welcome to room {currRoom}. Here, you will answer this puzzle question. {puzz1}: ")
        while answ1 != 'Footsteps':
            answ1 = input(f"Welcome to room {currRoom}. Here, you will answer this puzzle question. {puzz1}: ")
        if answ1 == 'Footsteps':
            #Giving the option to the player to go to a specified direction. The only possible being left or right. It is intended that the user put one of the two values.
            direction = input(f'Congrats, you have passed the first puzzle, you can choose to move between L/R: ')
            if direction == 'L':
                currRoom = 3
            else:
                currRoom = 2
    #Creating outcome for 3
    if currRoom == 3:
        answ3 = input(f"Welcome to room {currRoom}. Here, you will answer this puzzle question. {puzz3}: ")
        while answ3 != 'Map':
            answ3 = input(f"Welcome to room {currRoom}. Here, you will answer this puzzle question. {puzz3}: ")
        if answ3 == "Map":
            #Now the only possible direction is L, obligating the user to make this.
            direction = input(f':,( Bad luck... room {currRoom} does not have anything! You can choose to move L: ')
            while direction != "L":
                direction = input("You can't do that, let's move L: ")
                if direction == 'L':
                    currRoom = 1
    # As riddle 1 has been already answered, we can keep going to the next room.
    if currRoom == 1:
        direction = input(f"You already answered the room {currRoom} riddle, let's go R: ")
        while direction != "R":
            direction = input("There is nothing in that room, let's move R: ") #Here the program doesn't let the user go back to the room, since there is no exit there.
            if direction == 'R':
                currRoom = 2
    #Answering riddle 2.
    if currRoom == 2:
        answ2 = input(f"Welcome to room {currRoom}. Here, you will answer this puzzle question. {puzz2}: ")
        while answ2 != 'Seven':
            answ2 = input(f"Welcome to room {currRoom}. Here, you will answer this puzzle question. {puzz2}: ")
        if answ2 == "Seven":
            direction = input(f'Nice! Now you can choose to move U/D: ') # Here, the user chooses direction again between up and down.
            if direction == 'U':
                currRoom = 4
            else:
                currRoom = 5
    #In case the user goes up, they respond the following riddle.
    if currRoom == 4:
        answ4 = input(f"Welcome to room {currRoom}. Here, you will answer this puzzle question. {puzz4} ")
        while answ4 != 'David':
            answ4 = input(f"Welcome to room {currRoom}. Here, you will answer this puzzle question. {puzz4}: ")
        if answ4 == "David":
            direction = input(f'Unlucky, {currRoom} is empty :( You can choose to move D: ')
        while direction != "D":
            direction = input("Come on, keep it going. Let's move D: ") #The user is obligated to move D
        if direction == 'D':
            currRoom = 2
    #As in room 1, the room is already answered and makes the user go foward.
    if currRoom == 2:
        direction = input(f"You are currently on room {currRoom}. Let's move D: ")
        while direction != "D":
            direction = input("Don't you want to finish the game?. Let's move D: ")
            if direction == 'D':
                currRoom = 5
    #Answering riddle 5
    if currRoom == 5:
        answ5 = input(f'You are on room {currRoom}. Our question here is simple. {puzz5}')
        if answ5 != player:
            print(f'You got to be serious...')
            currRoom = 1 #As this was the easiest question, if the user is not able to answer it correctly, the program restarts.
        if answ5 == player:
            currRoom = 6
            print("Congratulations, your treasure was getting out of the maze! :)") #Here the player is able to go out of the maze.





