from random import randrange




def run_guess(guess,answer):
	if 0<guess<12:
		if guess == answer:
			print('You are a genius')
			return True

	else:
		print('hey I said 1-10')
		return False
if __name__ == '__main__':
	answer = randrange(1,10)
	while True:
		try:
			guess = int(input('guess a number 1-10 : '))
			
			if run_guess(guess,answer):
				break
		except ValueError as e :
			raise e 
			print('please enter a number')
			continue

