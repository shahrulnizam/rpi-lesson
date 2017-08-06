from datetime import datetime
import random
 
print "Hello! My name is Python. I am a programming language."

name = raw_input("What's your name? ")
 
print "It's nice to meet you " + name + "!"
  
year = raw_input("What's your year of birth? ") 
age = datetime.now().year - int(year)
 
print "You are " + str(age) + " years old!"
print "I was created in 1989, I'm " + str(datetime.now().year - 1989) + " years old!"
print "Let's play a game! I'll choose a number between 0 and 10. Try to guess it! You have 5 chances!"
 
for x in range(0,5):	
	python_number = random.randint(0,10)
	your_number = raw_input("Your guess: ")
 
	if python_number == int(your_number):
		print "You won! My number was " + str(python_number)
	else:
		print "You loose! My number was " + str(python_number)
 
print "It's already " + str(datetime.now().hour) + ":" + str(datetime.now().minute) + "! I have to go now"
