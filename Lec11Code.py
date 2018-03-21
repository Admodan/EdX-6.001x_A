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

#'''
#Lecture 11 Problem 4
#Given code below, define two methods for coordinate class:
#    __eq__ : returns true if coordinates same point on plane.
#    __repr__: returns string looks like valid python expression/
#    used to recreate an object with same value.
#   In other words, eval(repr(c)) ==c
#'''
#class Coordinate(object):
#    def __init__(self, x, y):
#        self.x = x
#        self.y = y

#    def getX(self):
#        # Getter method for a Coordinate object's x coordinate.
#        # Getter methods are better practice than just accessing an attribute directly
#        return self.x

#    def getY(self):
#        # Getter method for a Coordinate object's y coordinate
#        return self.y

#    def __eq__(self, other):
#        if self.x == other.x and self.y == other.y:
#            return True
#        else:
#            return False

#    def __repr__(self):
#        return 'Coordinate({},{})'.format(self.x, self.y)


#    def __str__(self):
#        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

#t = Coordinate(10,10)
#s = Coordinate(1,1)
#q = Coordinate(1,1)

#Lecture 11 Problem 5:
#Define intersect method which returns new intSet which contains
#only the elements present in both sets.
#Add method so that len(s) returns number of elements in s.

#class intSet(object):
#    """An intSet is a set of integers
#    The value is represented by a list of ints, self.vals.
#    Each int in the set occurs in self.vals exactly once."""

#    def __init__(self):
#        """Create an empty set of integers"""
#        self.vals = []

#    def __len__(self):
#        return len(self.vals)

#    def insert(self, e):
#        """Assumes e is an integer and inserts e into self"""
#        if not e in self.vals:
#            self.vals.append(e)

#    def member(self, e):
#        """Assumes e is an integer
#        Returns True if e is in self, and False otherwise"""
#        return e in self.vals

#    def remove(self, e):
#        """Assumes e is an integer and removes e from self
#        Raises ValueError if e is not in self
#        self.vals.remove() uses the remove method that is 
#        assosiated with lists. This is different from our 
#        function definition for remove. 
#        """
#        try:
#            self.vals.remove(e)
#        except:
#            raise ValueError(str(e) + ' not found')

#    def intersect(self, other):
#        ''' Assumes each member of the lists to be intersected
#        only occurs once. Returns a list containing only the 
#        memebers which occur in both lists.'''
#        intersectList = intSet()
#        for e in self.vals:
#            if e in other.vals:
#                intersectList.insert(e)
#        if len(intersectList) == 0:
#            return {}
#        return intersectList


#    def __str__(self):
#        """Returns a string representation of self"""
#        self.vals.sort()
#        return '{' + ','.join([str(e) for e in self.vals]) + '}'

#s1 = intSet()
#s = intSet()
#print (s)
#s.insert(3)
#s.insert(4)
#s.insert(6)
#s.insert(7)
#s1.insert(3)
#s1.insert(4)
#s1.insert(6)
#s1.insert(7)
#s.insert(3)
#print s
#s.member(3)
#s.member(5)
#s.insert(6)
#print s
#s.remove(3)
#print s
#s.remove(3)

#Lecture 11 Problem 6
#Create a class with three methods:
#__init__ method which initilizes the Queue object.
#insert: inserts one element into your Queue.
#remove: Pops first element in the queue. First in first out.
#If queue is empty raise a value error.
#My code below:

#class Queue(object):
#    def __init__(self):
#        self.lineup = []

#    def insert(self, e):
#        self.lineup.append(e)

#    def remove(self):
#        try:
#            return self.lineup.pop(0)
#        except:
#            raise ValueError

#Tests:
#q1 = Queue()
#q1.insert(12)
#q1.insert(3)
#q1.insert(2)
#q1.remove()
#q1.remove()
#q1.remove()
#q1.remove()

#Answer code:
#class Queue(object):

#    def __init__(self):
#        "Initializes 1 attribute: a list to keep track of the queue's elements"
#        self.qlist = []

#    def insert(self, element):
#        "Adds an element to the attribute list using append"
#        self.qlist.append(element)

#    def remove(self):
#        "Removes an element from the attribute list"
#        # Check if the list is empty; if so then raise a ValueError
#        if self.qlist == []:
#            raise ValueError()
#        else:
#            # Otherwise we want to remove the first element from the list
#            # and return that to the user.
#            element = self.qlist[0]
#            self.qlist.remove(element)
#            return element
#            # Could also do this in 1 line:
#            # return self.qlist.pop(0)

