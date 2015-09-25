#!/usr/bin/env python
def print_history(name, age, username):
	print "%s is %s years old, and username is %s"%(name, age, username)
def print_info(name, age, username):
	print "Your name is %s, you are %s years old, and your username is %s"%(name, age, username)
def main():
	history = []	
	try:
		f_before = open("log.txt", "r")
		history = f_before.readlines()
		f_before.close()
	except:
		pass # log.txt would not exist if program was first executed or terminated abnormally
	for cur in history:
		cur = cur.replace("\n", "").split("|")
		if len(cur) is not 3:
			open("log.txt", "wb").close()
			break
		print_history(cur[0], cur[1], cur[2])
	if len(history):
		print "\nAnd... you are?"
	name, age, username = raw_input("Name: "), raw_input("Age: "), raw_input("User name: ")
	print_info(name, age, username)
	f = open("log.txt", "a")
	f.write(name+"|"+age+"|"+username+"\n")
	f.close()
#try:
main()
#except:
#print "\nbye :)"
