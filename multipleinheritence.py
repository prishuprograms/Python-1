# Creating Classes A, B and C
# MultipleInheritence concept

# Class A
class A(object):
    def __init__(self):
        super().__init__()
        self.a = 'a'
        print(self.a)

# Class B
class B(object):
    def __init__(self):
        super().__init__()
        self.b='b'
        print(self.b)

# Class C
class C(B,A):
    def __init__(self):
        super().__init__()
        self.c = 'c'
        print(self.c)


c = C()
# ==== Code Ended ====
