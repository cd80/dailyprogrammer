#!/usr/bin/env python
'''
create a program that will allow you to enter events organizable by hour. There must be menu options of some form, and you must be able to easily edit, add, and delete events without directly changing the source code.
(note that by menu i dont necessarily mean gui. as long as you can easily access the different options and receive prompts and instructions telling you how to use the program, it will probably be fine)
'''

'''
specs
	menu
		add
		edit
		delete
		view
'''
def add_event():
	print "Add event"
def edit_event():
	print "Edit event"
def delete_event():
	print "Delete event"
def list_event():
	print "List event"
def exit_prog():
	print "Exit prog"
	exit()
def menu_main():
	print "1. Add new event"
	print "2. Edit event"
	print "3. Delete event"
	print "4. List events"
	print "5. Exit"
main_handle = [add_event, edit_event, delete_event, list_event, exit_prog]

def main():
	while 1:
		menu_main()
		menu_choice = raw_input("> ")
		try:
			menu_choice = int(menu_choice)
			main_handle[menu_choice-1]
		except: continue
		main_handle[menu_choice-1]()
if __name__ == '__main__':
	main()
