import string
import time
import random
from NumString import Numstring
import numpy as np
import matplotlib.pyplot as plt
if __name__ == '__main__':
	

	numstring_times = []
	regstring_times = []

	numstring = Numstring("abc")
	regstring = ""

	for i in range(0, 10000):
		char_to_add = random.choice(string.ascii_letters)
		
		start_time = time.time()
		numstring.append(char_to_add)
		end_time = time.time()

		numstring_times.append(end_time-start_time)

		start_time = time.time()
		regstring = char_to_add + regstring
		end_time = time.time()

		regstring_times.append(end_time-start_time)

	plt.plot(numstring_times, label="Numstring")
	plt.plot(regstring_times, label="Regular strings")
	plt.legend()
	plt.show()

	numstring_times = []
	regstring_times = []

	numstring = Numstring("abc")
	regstring = "abc"

	numstring_to_compare = Numstring("abd")
	regstring_to_compare = "abd"

	for i in range(0, 100000):
		char_to_add = random.choice(string.ascii_letters)
		
		numstring.appendleft(char_to_add)
		numstring_to_compare.appendleft(char_to_add)		
		regstring = char_to_add + regstring
		regstring_to_compare = char_to_add + regstring_to_compare

		start_time = time.time()
		numstring_to_compare.compare(numstring)
		end_time = time.time()
		numstring_times.append(end_time-start_time)

		start_time = time.time()
		regstring_to_compare == regstring
		end_time = time.time()
		regstring_times.append(end_time-start_time)

	plt.plot(numstring_times, label="Numstring")
	plt.plot(regstring_times, label="Regular strings")
	plt.legend()
	plt.show()