import random

def get_range (): 
	range_start = int (input ("Lower boundary:"))
	range_end = int (input ("Upper boundary:"))
	while (range_start >= range_end):
		print ("Are you retarded or something?")
		range_start = int (input ("Lower boundary:"))
		range_end = int (input ("Upper boundary:"))
	return (range_start, range_end)

def get_random_number (range_start, range_end):
	random_number = random.randint(range_start, range_end)
	print (range_start," <= NUMBER <= ",range_end)
	return (random_number)

def play_round (range_start, range_end, random_number):
	num_of_guesses = 0
	while True:
		guessed_number = int (input ("Guess:"))
		num_of_guesses+=1
		if (guessed_number < range_start or guessed_number > range_end):
			print ("Guessed number is outside of the range.")
		elif (guessed_number < random_number):
			print ("Guess higher")
		elif (guessed_number > random_number):
			print ("Guess lower")
		else:
			print ("YOU'VE DIDEN IT")
			return (num_of_guesses)
			
def main ():
	range_start, range_end = get_range() 
	random_number = get_random_number (range_start, range_end)
	num_of_guesses = play_round (range_start, range_end, random_number)
	return (num_of_guesses)

while True:
	num_of_guesses = main()
	print ("Your score was", num_of_guesses, " guesses.")
	if (input ("Play again? Y for yes.") != ("Y" and "y")):
		break
