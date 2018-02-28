'''
L11 Problem 2
'''
#class Clock(object):
#    def __init__(self, time):
#        self.time = time
#        print('Time in __init__:', time)
#        print('self.time in __init__', self.time)
#    def print_time(self):
#        time = '6:30'
#        print('Time in print_time:', time)
#        print('self.time in print_time', self.time)
#        print (self.time)

#clock = Clock('5:30')
#clock.print_time()

'''
Lecture 11 Problem 3
Give the outputs and their type.
'''
#class Weird(object):
#    def __init__(self, x, y): 
#        self.y = y
#        self.x = x
#    def getX(self):
#        return x 
#    def getY(self):
#        return y

#class Wild(object):
#    def __init__(self, x, y): 
#        self.y = y
#        self.x = x
#    def getX(self):
#        return self.x 
#    def getY(self):
#        return self.y

#X = 7
#Y = 8

#'''3.1'''
#w1 = Weird(X, Y)
#print (w1.getX())

#'''3.2'''
#print (w1.getY())

#'''3.3'''
#w2 = Wild(X, Y)
#print (w2.getX())

#'''3.4'''
#print (w2.getY())

#'''3.5'''
#w3 = Wild(17, 18)
#print (w3.getX())

#'''3.6'''
#print (w3.getY())

#'''3.7'''
#w4 = Wild(X, 18)
#print (w4.getX())

#'''3.8'''
#print (w4.getY())

#'''3.9'''
#X = w4.getX() + w3.getX() + w2.getX()
#print X

#'''3.10'''
#print (w4.getX())

#'''3.11'''
#Y = w4.getY() + w3.getY()
#Y = Y + w2.getY()
#print (Y)

#'''3.12'''
#print (w2.getY())

'''
Lecture 11 Problem 4
Given code below, define two methods for coordinate class:
    __eq__ : returns true if coordinates same point on plane.
    __repr__: returns string looks like valid python expression/
    used to recreate an object with same value.
   In other words, eval(repr(c)) ==c
'''
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'