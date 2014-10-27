ten_things = "Apples Oranges Crows Telephone Light Sugar"
print "Wait there's not 10 things on that list. Let's fix that."

stuff = ten_things.split(" ")
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding:", next_one
    stuff.append(next_one)
    print "There are now %d items in the list" % len(stuff)

print "There we go. The list now has 10 items. This is the list: ", stuff

print "Let's do some things with stuff"
print stuff[1]
print stuff[-1] #whoa
print stuff.pop()
print ''.join(stuff)
print '#'.join(stuff[3:7])