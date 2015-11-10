print "Welcome to the Survey!"
name = raw_input("What is your name?")
color = raw_input("What is your favorite color?")
hobby = raw_input("what is your favorite hobby?")
movie = raw_input("What is your favorite movie?")
animal = raw_input("what is your favorite animal?")
city = raw_input("What is your favorite city?")
print name + "'s favorite color is" + " " + color
print "%s's favorite hobby is %s" % (name, hobby)
print "%s's favorite movie is %s" % (name, movie)
print "%s's favorite animal is %s" % (name, animal)
print "%s's favorite city is %s" % (name, city)
