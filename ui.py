# events-example0.py
# Barebones timer, mouse, and keyboard events

from tkinter import *

# Initialize the data which will be used to draw on the screen.
def init(data):
	# load data as appropriate
	data.height = 1440/2
	data.width = 2304/2
	pass

# controllers ################################
def mousePressed(event, data):
	# use event.x and event.y
	pass

def keyPressed(event, data):
	# use event.char and event.keysym
	pass

def timerFired(data):
	pass


# view #######################################
def redrawAll(canvas, data):
	# draw in canvas
	pass



def run(width=300, height=300):
	def redrawAllWrapper(canvas, data):
		canvas.delete(ALL)
		redrawAll(canvas, data)
		canvas.update()    

	def mousePressedWrapper(event, canvas, data):
		mousePressed(event, data)
		redrawAllWrapper(canvas, data)

	def keyPressedWrapper(event, canvas, data):
		keyPressed(event, data)
		redrawAllWrapper(canvas, data)

	def timerFiredWrapper(canvas, data):
		timerFired(data)
		redrawAllWrapper(canvas, data)
		# pause, then call timerFired again
		canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
		
	# Set up data and call init
	class Struct(object): pass
	data = Struct()
	
	data.timerDelay = 100 # milliseconds
	init(data)
	# create the root and the canvas
	root = Tk()
	canvas = Canvas(root, width=data.width, height=data.height)
	canvas.pack()
	# set up events
	root.bind("<Button-1>", lambda event:
							mousePressedWrapper(event, canvas, data))
	root.bind("<Key>", lambda event:
							keyPressedWrapper(event, canvas, data))
	timerFiredWrapper(canvas, data)
	# and launch the app
	root.mainloop()  # blocks until window is closed
	print("bye!")

run()
