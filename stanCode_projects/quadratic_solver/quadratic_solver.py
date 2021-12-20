"""
File: quadratic_solver.py
Name:
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	1. assign all the elements we need
		(print, a, b, c, discriminant, math.sqrt, numerator & denominator)
	2. def if dis. < 0 => directly print ('No real roots')
	3. def three different conditions
		dis. > 0
		dis. = 0
		dis. < 0
	"""
	# assign
	print("stanCode Quadratic Solver!")
	a = int(input("Enter a: "))
	b = int(input("Enter b: "))
	c = int(input("Enter c: "))
	discriminant = (b * b) - (4 * a * c)
	# To prevent negative discriminant from entering math.sqrt
	if discriminant < 0:
		print('No real roots')
	else:
		math_sqrt = math.sqrt(discriminant)
		numerator1 = -b + math_sqrt
		numerator2 = -b - math_sqrt
		denominator = 2 * a
		x1 = numerator1 / denominator
		x2 = numerator2 / denominator
		# three conditions
		if discriminant > 0:
			print('Two roots= ' + str(x1) + ' , ' + str(x2))
		elif discriminant == 0:
			math.sqrt(discriminant)
			print('One root= ' + str(x1))
		else:
			print('No real roots')











###### DO NOT EDIT CODE BELOW THIS LINE ######


if __name__ == "__main__":
	main()
