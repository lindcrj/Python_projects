"""
File: prime_checker.py
Name:
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
	"""
	Prime numbers can only be divisible by themselves and 1
	=> number N % 2, 3, 4, 5, ... N-1 != 0
	"""
	print('Welcome to prime checker!')
	while True:
		divisor = 2
		number = int(input('n: '))
		if number == EXIT:
			print('Have a good one!')
			break
		else:
			while number % divisor != 0:
				divisor += 1
			if divisor == number:
				print(str(number) + ' is a prime number.')
			else:
				print(str(number) + ' is not a prime number.')








###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
