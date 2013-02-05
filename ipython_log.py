# IPython log file

# This is a session of what I call 'discover'/'digging' science. Quickly looking at
# data at different angles in order to get a feel of it.
# Actually, it is an intro to "functional"-style python. functional in "" just
# to satisfy any lispers or haskellers.

# Notes:
# All calls to 'get_ipython().magic' are 'ipython magic commands' I used, these
# are the ones starting with a '%'-sign. The ones I used are, in order:
# ipython> f.read?
# ipython> %logstart
# ipython> _ = ... (don't remember)

# Unfortunately, I am not allowed to give you the full data. Here is a small
# part of it (remember 'fair use' ;))
#
#Insult,Date,Comment
#1,20120618192155Z,"""You fuck your dad."""
#0,20120528192215Z,"""i really don't understand your point.\xa0 It seems that you are mixing apples and oranges."""
#0,,"""A\\xc2\\xa0majority of Canadians can and has been wrong before now and will be again.\\n\\nUnless you're supportive of the idea that nothing is full proof or perfect so you take your chances and if we should inadvertently kill your son or daughter then them's the breaks and we can always regard you as collateral damage like in wartime - and sorry, but\\xc2\\xa0the cheques in the mail. """
#0,,"""listen if you dont wanna get married to a man or a women DONT DO IT. what would it bother you if gay people got married stay in your lane do you let them do them. And your god is so nice but quick to judg if your not like him, thought you wasnt suppose to judge people."""
#0,20120619094753Z,"""C\xe1c b\u1ea1n xu\u1ed1ng \u0111\u01b0\u1eddng bi\u1ec3u t\xecnh 2011 c\xf3 \xf4n ho\xe0 kh\xf4ng ? \nC\xe1c ng\u01b0 d\xe2n ng\u1ed3i cu\xed \u0111\u1ea7u chi\u1ee5 nh\u1ee5c c\xf3 \xf4n ho\xe0 kh\xf4ng ?\nC\xe1c n\xf4ng d\xe2n gi\u1eef \u0111\u1ea5t \u1edf V\u0103n Giang, C\u1ea7n Th\u01a1 c\xf3 \xf4n ho\xe0 kh\xf4ng ?\n.................\nR\u1ed1t cu\u1ed9c \u0111\u01b0\u1ee3c g\xec\xa0 th\xec ch\xfang ta \u0111\xe3 bi\u1ebft !\nAi c\u0169ng y\xeau chu\u1ed9ng ho\xe0 b\xecnh, nh\u01b0ng \u0111\xf4i khi ho\xe0 b\xecnh ch\u1ec9 th\u1eadt s\u1ef1 \u0111\u1ebfn sau chi\u1ebfn tranh m\xe0 th\xf4i.\nKh\xf4ng c\xf2n con \u0111\u01b0\u1eddng n\xe0o ch\u1ecdn kh\xe1c \u0111\xe2u, \u0111\u1eebng m\u01a1 th\xeam n\u01b0\xe3."""
#0,20120620171226Z,"""@SDL OK, but I would hope they'd sign him to a one-year contract to start with. Give him the chance to be reliable and productive, but give themselves the out if all his time off has hurt his playing skills or if he falls back into old habits."""
#0,20120503012628Z,"""Yeah and where are you now?"""
#1,,"""shut the fuck up. you and the rest of your faggot friends should be burned at the stake"""
#1,20120502173553Z,"""Either you are fake or extremely stupid...maybe both..."""

# Opens a file, doesn't read from it.
f = open('insults.csv')
f
get_ipython().magic(u'pinfo f.read')
# Read the whole file content and return it as a string. This is how easy it can be.
f.read()

# Utility to read .csv files. 'Comma Separated Values' are quite widespread in
# science. It is also an ugly format which everybody interprets differently.
import csv
rdr = csv.DictReader(open('insults.csv'))
for line in rdr:
    # 'line' is a dict(ionary), which is just a key/value store. Also known as
    # map, hashmap, hashtable, table, ...
    # line['Date'] accesses the date field, etc.
    print(line)

# Gotta reopen it since the loop above read it all!
rdr = csv.DictReader(open('insults.csv'))
get_ipython().magic(u'logstart')

# This is a generator, known as 'lazy sequence' in other functional languages.
# It does not store the numbers from 0 to 9, but rather is some funky object
# which yields all of these numbers one after the other.
# Usually people say it's good for having 'infinite sequences', while this is
# true, it doesn't ring a bell if you don't know it. You could see a good
# argument for generators being that they use less memory since they only have
# one element in memory at any time!
# Infinite sequence is for when you need something like cycles or so. [1, 2, 1,
# 2, 1, 2, ...]
(i for i in range(10))
# You can transform it to a list in order to have all objects.
list((i for i in range(10)))
# This gives us the whole file as a list of dicts.
# If you program this way, you rarely need classes, all you need is lists and
# dicts.
raw_data = list(rdr)
raw_data
# We use filter to get all entries of the list where the 'lambda' function is
# True. A 'lambda function' is basically a one-liner function with a few gists.
# 'lambda' is the real name of that #-thingy in Mathematica.
# So here, we get all the lines which are insults.
insults = filter(lambda datum: datum['Insult'] == '1', raw_data)
# And look at it.
len(insults)
len(raw_input)
len(raw_data)
insults
# Now I want to be sure that I got it right, do all entries of 'insults' have
# the 'Insult'-field set to 1? Let's look at it
map(lambda datum: datum['Insult'], insults)
# Oops, way too many, and
# oops2, it's all strings! Want to get it as a number. 'int(foo)' casts 'foo' into an int.
map(lambda datum: int(datum['Insult']), insults)
# 'all' returns true if every entry is a truthy value. 1 is truthy. Note that
# '0' (the string "0") is truthy too, that's why the int cast was important!
# The empty string is the only falsy string!
all(map(lambda datum: int(datum['Insult']), insults))
insults
# Now I want to look at the kinds of insults that were made...
map(lambda datum: datum['Comment'], insults)
'\n'.join(map(lambda datum: datum['Comment'], insults))
# Holy c...!
get_ipython().magic(u'edit _')
