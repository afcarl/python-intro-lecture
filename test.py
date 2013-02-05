# Here I want to show the advanced guys of you that foo.bar() and bar(foo) can
# be the same. Polymorphism is just a special case of multiple-dispatching. I'm
# not saying python has multiple dispatching, it hasn't.
# This example might still 'enlighten' some, hopefully.. :)
import sys

# This is what 'str' could look like, in your mind:
# class str:
#     def strip(self):
#         pass

# This is how you'd call it the regular way
"foo".strip()

# Or if you prefer:
# foo = "foo"
# foo.strip()

# This just reads lines from stdin, press CTRL+D to exit the loop. Or pipe some
# lines into the call using bash | and/or <
for line in sys.stdin:
    # Now this is the interesting part. Look at how the function 'str.strip' is
    # applied to the string objects. What happens in the background is this:
    #
    # str.strip(word)
    #
    # as opposed to
    #
    # word.strip()
    print(map(str.strip, line.split(' ')))

# If you found this pointless, don't worry. Sooner or later you'll remember this :)
