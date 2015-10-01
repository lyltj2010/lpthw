# close: Closes the file
#read: Reads the contents of the file
#readline: Reads just one line of a text file
#truncate: Empties the file.
#write("stuff"): Writes "sruff" to the file

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C(^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Noe I'm going to ask you for three lines."

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I'm goint to write these to the file."
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")
#target.write(line1+"\n"+line2+"\n"+line3+"\n")
target.write("%s\n%s\n%s" % (line1, line2, line3))
print "And finally, we colse it."
target.close()
