# template for "Stopwatch: The Game"
import simplegui

# define global variables
t = 0
x = 0
y = 0
z = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    if (t < 10):
        t = '0:00.'+str(t)
        return t
    elif((t > 9) and (t < 100)):
        t = '0:0' + str(t / 10) + '.' + str(t % 10)
        return t
    elif((t > 99) and (t < 600)):
        t = '0:' + str(t / 10) + '.' + str(t % 10)
        return t
    else:
        if(((t % 600) / 10) < 10):
            t = str(t / 600) + ':0' + str((t % 600) / 10) + '.' + str(t % 10)
            return t
        else:
            t = str(t / 600) + ':' + str((t % 600) / 10) + '.' + str(t % 10)
            return t
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global z
    z = True
    timer.start()
    
def stop():
    global x, y, z
    if (z == True):
        if((t % 10) == 0):
            x +=1
            y +=1
        else:
            y +=1
        timer.stop()
        z = False
    else:
        timer.stop()
        
    
def reset():
    timer.stop()
    global t, x, y
    t = 0
    x = 0
    y = 0
    

# define event handler for timer with 0.1 sec interval
def stopwatch():
    global t
    t += 1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(t), [40, 100], 50, 'White')
    global x, y
    canvas.draw_text(str(x) + '/' + str(y), [150, 25], 30, 'Red')
    
# create frame
frame = simplegui.create_frame('Stop Watch', 200, 200)

# register event handlers
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100, stopwatch)
button1 = frame.add_button('Start', start)
button2 = frame.add_button('Stop', stop)
button3 = frame.add_button('Reset', reset)

# start frame
frame.start()
# Please remember to review the grading rubric
