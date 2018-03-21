''' L12 Problem 2'''
class A(object):
    def __init__(self):
        self.a = 1
    def x(self):
        print "A.x"
    def y(self):
        print "A.y"
    def z(self):
        print "A.z"

class B(A):
    def __init__(self):
        A.__init__(self)
        self.a = 2
        self.b = 3
    def y(self):
        print "B.y"
    def z(self):
        print "B.z"

class C(object):
    def __init__(self):
        self.a = 4
        self.c = 5
    def y(self):
        print "C.y"
    def z(self):
        print "C.z"

class D(C, B):
    def __init__(self):
        C.__init__(self)
        B.__init__(self)
        self.d = 6
    def z(self):
        print "D.z"

'''
Important lesson here. Look at code and notice what
obj.a prints. It will print 2. This is because as the 
code runs through the __init__ methods of each object
self.a is overwritten. So the last method to define 
self.a is the value that will remain. This is different 
from inheritance of methods. When obj.y() is called the method
is inherited depth first, left to right. Meanning that the 
code looks through the methods of C first, then C's superclasses,
then looks through B and B's superclasses. Once it finds an 
answer it stops. 
'''
print obj.a 
print obj.b
print obj.c
print obj.d
obj.x()
obj.y()
obj.z()