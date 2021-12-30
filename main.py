# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# content of test_sample.py
def inc(x):
    print("This is a new test")
    return x + 1


def test_answer():
    print("This one is a new line")
    assert inc(3) == 3

def inc2(x):
    print("This is a new test")
    return x + 1

def test_answer2():
    print("This one is a new line")
    assert inc(3) == 3

def test_mul():
    assert 3*5 == 15

def test_div():
    assert 10%4 == 2



class HelloWorld():
    def __init__(self, name):
        self.name = name

    def pritnName(self):
        print(self.name)
