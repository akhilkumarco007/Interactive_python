# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math
num_range = 100

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    
    low = 0 
    global num_range
    high = num_range
    global n
    n = math.ceil(math.log(high - low, 2))
    print
    print "New game. Range is 0 to "+str(num_range)
    if (num_range == 100):
        global secret_number
        secret_number = random.randrange(0, 100)
        print "Number of remaining guesses is "+str(n)
    else:
        secret_number = random.randrange(0, 1000)
        print "Number of remaining guesses is "+str(n)
    


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    
    global num_range
    num_range = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    
    global num_range
    num_range = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    print
    selected_number = int(guess)
    print "Guess was "+guess
    
    global n
    n = n - 1 
    print "Number of remaining guesses is "+str(n)
    global secret_number
    if (secret_number == selected_number):
        print "Correct"
        new_game()
    elif (secret_number > selected_number):
        if (n == 0):
            new_game()
        else:
            print "Higher"
    else:
        if (n == 0):
            new_game()
        else:
            print "Lower"
        
    
    
# create frame
frame = simplegui.create_frame("Guess the Number", 200, 200)

# register event handlers for control elements and start frame

restart = frame.add_button("Restart", new_game, 100)
range1 = frame.add_button("Range is [0,100)", range100, 200)
range2 = frame.add_button("Range is [0,1000)", range1000, 200)
inp = frame.add_input("Your Input", input_guess, 50)
# call new_game 
new_game()

frame.start()
# always remember to check your completed program against the grading rubric
