# parentheses '(' are tuples, square-brackets '[' are lists
profs = ('Bientinesi', 'Leibe', 'Lichter', 'Lucasius')

# if-in checks whether the string 'Lucas' is in the tuple/list/whatever
if 'Lucas' in profs:
    print('Lucas is a professor')
else:
    print('Lucas is not a prof')


# As you'd expect
if 'Lucas' not in profs:
    print("yeah, that's right")


# This is a for-in loop. 'prof' will be each of the elements one after the other.
for prof in profs:
    print(prof + ' is a professor')


# Here are the square brackets, finally. This is a list.
presents = ['wine', 'cheese', 'crap']
for present in presents:
    # Note that you can mix/match and even change the type as you whish.
    # Important: 'present' is actually a copy of the lists element, not a
    # pointer/reference. Modifying it does not modify the list as you will see
    # in the print statement below!
    present = 5

# ' '.join(presents) creates a string with all elements from the list
# 'presents' combined, using a space ' ' as glue between the elements.

# somestring.split(' ') is the opposite: it creates a list by splitting
# 'somestring' at every occurence of a space ' '.
print(' '.join(presents).split(' '))


occurrences = 5
# This defines the function 'doit', taking no arguments. (No need to declare
# the return value.)
def doit():
    # Intentional typo.
    occurences = 7

# Note that occurrences stays the same, and you get no warning or error! This
# is because setting and declaring a variable has the same syntax. The typo
# inside 'doit' might be hard to spot!
print(occurrences)
doit()
print(occurrences)
