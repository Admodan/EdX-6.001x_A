#''' L12 Problem 2'''
#class A(object):
#    def __init__(self):
#        self.a = 1
#    def x(self):
#        print "A.x"
#    def y(self):
#        print "A.y"
#    def z(self):
#        print "A.z"

#class B(A):
#    def __init__(self):
#        A.__init__(self)
#        self.a = 2
#        self.b = 3
#    def y(self):
#        print "B.y"
#    def z(self):
#        print "B.z"

#class C(object):
#    def __init__(self):
#        self.a = 4
#        self.c = 5
#    def y(self):
#        print "C.y"
#    def z(self):
#        print "C.z"

#class D(C, B):
#    def __init__(self):
#        C.__init__(self)
#        B.__init__(self)
#        self.d = 6
#    def z(self):
#        print "D.z"

#'''
#Important lesson here. Look at code and notice what
#obj.a prints. It will print 2. This is because as the 
#code runs through the __init__ methods of each object
#self.a is overwritten. So the last method to define 
#self.a is the value that will remain. This is different 
#from inheritance of methods. When obj.y() is called the method
#is inherited depth first, left to right. Meanning that the 
#code looks through the methods of C first, then C's superclasses,
#then looks through B and B's superclasses. Once it finds an 
#answer it stops. 
#'''
#print obj.a 
#print obj.b
#print obj.c
#print obj.d
#obj.x()
#obj.y()
#obj.z()


#Lecture 12 Example. Building a Class List
'''
The code below includes all the code to create students,
undergrad and grad, person, transfer students and grades
in order to populate a class list of all students in the 
class and their grades. The code that prints the class list
returns a copy of the list which is not the best practice 
because it will be expensive if the class is large. Also python
allows us to directly access the class data unlike other programming
languages. This can be handy but it is also dangerous because 
we can change the data when we access the attributes of the objects. 

'''

import datetime

class Person(object):
    def __init__(self, name):
        """create a person called name"""
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]

    def getLastName(self):
        """return self's last name"""
        return self.lastName

    def setBirthday(self,month,day,year):
        """sets self's birthday to birthDate"""
        self.birthday = datetime.date(year,month,day)

    def getAge(self):
        """returns self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        """return True if self's ame is lexicographically
           less than other's name, and False otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        """return self's name"""
        return self.name

# me = Person("William Eric Grimson")
# print me
# me.getLastName()
# me.setBirthday(1,2,1927)
# me.getAge()
# her = Person("Cher")
# her.getLastName()
# plist = [me, her]
# for p in plist: print p
# plist.sort()
# for p in plist: print p

class MITPerson(Person):
    nextIdNum = 0 # next ID number to assign

    def __init__(self, name):
        Person.__init__(self, name) # initialize Person attributes
        # new MITPerson attribute: a unique ID number
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    # sorting MIT people uses their ID number, not name!
    def __lt__(self, other):
        return self.idNum < other.idNum

# p1 = MITPerson('Eric')
# p2 = MITPerson('John')
# p3 = MITPerson('John')
# p4 = Person('John')

# print p1

# p1.getIdNum()
# p2.getIdNum()
# p1 < p2
# p3 < p2
# p4 < p1

# p1 < p4


class UG(MITPerson):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year

class Grad(MITPerson):
    pass

def isStudent(obj):
    return isinstance(obj,UG) or isinstance(obj,Grad)

#s1 = UG('Fred', 2016)
#s2 = Grad('Angela')
#isStudent(s1)
#isStudent(s2)

class TransferStudent(MITPerson):
    pass

# go back and define
# class Student(MITPerson)
# change inheritance for UG, Grad and TransferStudent
# change def isStudent(obj):
#            return isinstance(obj, Student)



class Grades(object):
    """A mapping from students to a list of grades"""
    def __init__(self):
        """Create empty grade book"""
        self.students = []  # list of Student objects
        self.grades = {}    # maps idNum -> list of grades
        self.isSorted = True # true if self.students is sorted

    def addStudent(self, student):
        """Assumes: student is of type Student
           Add student to the grade book"""
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False

    def addGrade(self, student, grade):
        """Assumes: grade is a float
           Add grade to the list of grades for student"""
        try:
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            raise ValueError('Student not in grade book')

    def getGrades(self, student):
        """Return a list of grades for student"""
        try:    # return copy of student's grades
            return self.grades[student.getIdNum()][:]
        except KeyError:
            raise ValueError('Student not in grade book')

    def allStudents(self):
        """Return a list of the students in the grade book"""
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:] #return copy of list of students

def gradeReport(course):
    """Assumes: course if of type grades"""
    report = []
    for s in course.allStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot/numGrades
            report.append(str(s) + '\'s mean grade is '
                          + str(average))
        except ZeroDivisionError:
            report.append(str(s) + ' has no grades')
    return '\n'.join(report)

ug1 = UG('Jane Doe', 2014)
ug2 = UG('John Doe', 2015)
ug3 = UG('David Henry', 2003)
g1 = Grad('John Henry')
g2 = Grad('George Steinbrenner')

six00 = Grades()
six00.addStudent(g1)
six00.addStudent(ug2)
six00.addStudent(ug1)
six00.addStudent(g2)

for s in six00.allStudents():
    six00.addGrade(s, 75)
six00.addGrade(g1, 100)
six00.addGrade(g2, 25)

six00.addStudent(ug3)

#print gradeReport(six00)





##Lecture 12 Problem 3
#'''
#This is an object oriented version of hand from the word game problem
#in Problem Set4. Your task is to implement the 'update' method.
#'''

#import random 

#class Hand(object):
#    def __init__(self, n):
#        '''
#        Initialize a Hand.

#        n: integer, the size of the hand.
#        '''
#        assert type(n) == int
#        self.HAND_SIZE = n
#        self.VOWELS = 'aeiou'
#        self.CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

#        # Deal a new hand
#        self.dealNewHand()

#    def dealNewHand(self):
#        '''
#        Deals a new hand, and sets the hand attribute to the new hand.
#        '''
#        # Set self.hand to a new, empty dictionary
#        self.hand = {}

#        # Build the hand
#        numVowels = self.HAND_SIZE / 3
    
#        for i in range(numVowels):
#            x = self.VOWELS[random.randrange(0,len(self.VOWELS))]
#            self.hand[x] = self.hand.get(x, 0) + 1
        
#        for i in range(numVowels, self.HAND_SIZE):    
#            x = self.CONSONANTS[random.randrange(0,len(self.CONSONANTS))]
#            self.hand[x] = self.hand.get(x, 0) + 1
            
#    def setDummyHand(self, handString):
#        '''
#        Allows you to set a dummy hand. Useful for testing your implementation.

#        handString: A string of letters you wish to be in the hand. Length of this
#        string must be equal to self.HAND_SIZE.

#        This method converts sets the hand attribute to a dictionary
#        containing the letters of handString.
#        '''
#        assert len(handString) == self.HAND_SIZE, "Length of handString ({0}) must equal length of HAND_SIZE ({1})".format(len(handString), self.HAND_SIZE)
#        self.hand = {}
#        for char in handString:
#            self.hand[char] = self.hand.get(char, 0) + 1


#    def calculateLen(self):
#        '''
#        Calculate the length of the hand.
#        '''
#        ans = 0
#        for k in self.hand:
#            ans += self.hand[k]
#        return ans
    
#    def __str__(self):
#        '''
#        Display a string representation of the hand.
#        '''
#        output = ''
#        hand_keys = self.hand.keys()
#        hand_keys.sort()
#        for letter in hand_keys:
#            for j in range(self.hand[letter]):
#                output += letter
#        return output

#    def update(self, word):
#        """
#        Does not assume that self.hand has all the letters in word.

#        Updates the hand: if self.hand does have all the letters to make
#        the word, modifies self.hand by using up the letters in the given word.

#        Returns True if the word was able to be made with the letter in
#        the hand; False otherwise.
        
#        word: string
#        returns: Boolean (if the word was or was not made)
#        """
#        # Your code here
#        raise NotImplementedError()

    
#myHand = Hand(7)
#print (myHand)
#print (myHand.calculateLen())

#myHand.setDummyHand('aazzmsp')
#print (myHand)
#print (myHand.calculateLen())

#myHand.update('za')
#print (myHand)

