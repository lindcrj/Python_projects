"""
File: rocket.py
Name:
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():
	"""
	Disassembled into different parts
	"""
	head()
	belt()
	upper()
	under()
	belt()
	head()


def head():
	"""
	Decreasing number of spaces
	Increasing number of '/\'
	"""
	for i in range(SIZE, 0, -1):  # 3, 2, 1
		for j in range(i):  # 3, 2, 1
			print(" ", end="")
		for j in range(i, SIZE+1):  # 1, 2, 3
			print('/', end="")
		for j in range(i, SIZE+1):  # 1, 2, 3
			print('\\', end="")
		print(" ")


def belt():
	"""
	One + at the beginning and the end
	The number of '=' is twice the SIZE
	"""
	ans = " "
	print('+', end="")
	for i in range(SIZE):
		print('==', end="")
	print('+')
	return ans


def upper():
	"""
	One '|' at the beginning and the end
	Decreasing number of '.', start from SIZE-1
	Increasing number of '/\'
	"""
	for i in range(SIZE, 0, -1):   # 3, 2, 1
		print('|', end="")
		for j in range(i-1, 0, -1):  # 2, 1
			print('.', end="")
		for j in range(i, SIZE+1):   # 1, 2, 3
			print('/\\', end="")
		for j in range(i-1, 0, -1):  # 2, 1
			print('.', end="")
		print('｜', end="")
		print("")


def under():
	"""
		One '|' at the beginning and the end
		Increasing number of '.', from 0 to SIZE-1
		Decreasing number of '/\'
		"""
	for i in range(SIZE, 0, -1):   # 3, 2, 1
		print('|', end="")
		for j in range(i+1, SIZE+1):  # 2, 1, 0
			print('.', end="")
		for j in range(i, 0, -1):  # 3, 2, 1
			print('\\/', end="")
		for j in range(i+1, SIZE+1):
			print('.', end="")
		print('｜', end="")
		print("")










###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()