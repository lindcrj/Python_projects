"""
File: weather_master.py
Name:
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
Exit = -1


def main():
	"""
	Average = temperature sum / input times
	"""
	print('stanCode \" Weather Master 4.0 \" !')
	temperature = int(input('Next Temperature: (or -1 to quit)? '))
	highest = temperature
	lowest = temperature
	if temperature == Exit:  # make sure temperature != Exit
		print('No temperatures were entered.')
	else:
		t = temperature
		cold = 0
		i = 0
		if temperature < 16:  # check whether the first input temperature < 16
			if temperature != Exit:
				cold += 1
		while True:  # loop the input until temperature == Exit
			temperature = int(input('Next Temperature: (or -1 to quit)? '))
			i += 1
			t += temperature
			if temperature < 16:
				if temperature != Exit:
					cold += 1
			if temperature == Exit:
				break
			if temperature > highest:
				highest = temperature
			if temperature < lowest:
				lowest = temperature
		sum_temp = t + 1
		average = sum_temp/i
		print('Highest temperature = ' + str(highest))
		print('Lowest temperature = ' + str(lowest))
		print('Average = ' + str(average))
		print(str(cold) + ' cold day(s)')



###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
