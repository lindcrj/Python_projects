"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:
	:return:
	"""
	if n//10 == 0:
		return n
	else:
		if n < 0:
			n *= -1
			num1 = n % 10
			num2 = (n // 10) % 10
			if num1 < num2:
				return find_largest_digit(n // 10)
			else:
				return find_largest_digit((n // 10) - num2 + num1)
		else:
			num1 = n % 10
			num2 = (n//10) % 10
			if num1 < num2:
				return find_largest_digit(n//10)
			else:
				return find_largest_digit((n // 10) - num2 + num1)
	








if __name__ == '__main__':
	main()
