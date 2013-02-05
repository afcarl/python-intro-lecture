#!/usr/bin/env python
# Duck typing and some more.


def foo(bar):
    # Note the 'foo.', meaning 'thing' will be a variable stored "inside" the
    # 'foo' function.
    print(foo.thing)


def baz(bar):
    bar = 3
    return bar


# Don't even remember what I wanted to show here, I think I didn't do that in class :)
foo.thing = 5
foo(baz(5))


# This is a simple class, no inheritance or interface!
class Dog:
    # This is python's constructor, always named '__init__'
    def __init__(self, name):
        # See comment below about 'self'.
        self.name = name

    # All methods need to take a first argument, which will contain the object
    # it is called on. You can name it whatever you like, but it's usually
    # called 'self'. This is a wink to C++ 'this', which the C++ compiler
    # passes implicitly, behind your back. Python favors expliciteness.
    # You'd think it's annoying to type, but in practice, it isn't.
    def sayit(self):
        # And you access attributes (some call it member variables) through
        # 'self'
        print("Wuff wuff, I am " + self.name)


# Cat just so happens to have the same interface as Dog, but there is no
# explicit inheritance or binding to an interface.
class Cat:
    def sayit(self):
        # All cats meow. They are not as full of themselves as dogs.
        print("Meow")


# Imagine this is some other class which happens to have the same interface as
# Dog and Cat, but this is unintentional.
class Microwave:
    def sayit(self):
        print("Qwak qwak")


# This is a function which works with any animal.
# In statically-typed OO-languages, you'd have to specify the type of 'animal'.
# Will it be Dog, Cat, or what? So one has to go back, add a common interface,
# make Dog and Cat implement it etc. What a cludge!
def poke(animal):
    # This will 'just work' for any object having a 'sayit' method taking no
    # arguments. Even for microwaves. If the object doesn't have such a method,
    # you'd get an exception thrown here.
    # C++ is trying hard to achive such a beauty through templates. While it
    # more-or-less works, the syntax and overhead are enormous.
    animal.sayit()

poke(Dog("Jim"))
poke(Cat())
poke(Microwave())
# So yeah, this will accept a microwave.
# "If it walks like a duck and quacks like a duck, it is a duck."
