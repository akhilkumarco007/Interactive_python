# implementation of card game - Memory

import simplegui
import random

deck = [0, 1, 2, 3, 4, 5, 6, 7] * 2
exposed = [False] * 16
count = 0

# helper function to initialize globals
def new_game():
    global state, count, exposed
    state = 0
    random.shuffle(deck)
    count = 0
    label.set_text("Turns = "+str(count))
    exposed = [False] * 16
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed, state, a, b, c, count
    a = pos[0]/50
    if state == 0:    
        exposed[a] = True
        b = a
        state = 1
    elif (state == 1) and (exposed[a] == False):
        if exposed[a] == False:
            exposed[a] = True
        state = 2
        count = count + 1
        label.set_text("Turns = "+str(count))
        c = a
    elif (state == 2) and (exposed[a] == False):
        if deck[b] != deck[c]:
            exposed[b] = False
            exposed[c] = False
        if exposed[a] == False:
            exposed[a] = True
        b = a
        state = 1
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(len(deck)):
        if exposed[i]:
            canvas.draw_text(str(deck[i]), [16 + 50 *(i), 60], 40, 'White')
        else:
            canvas.draw_polygon([((25 + 50 *(i)) - 24, 0), ((25 + 50 *(i)) + 24, 0), ((25 + 50 *(i)) + 24, 100), ((25 + 50 *(i)) - 24, 100)], 1, 'Green', 'Green')

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric