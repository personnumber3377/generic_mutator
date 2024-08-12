

from generic_mutator import *

if __name__=="__main__":
	input_data = "somedata"
	COUNT = 100
	for _ in range(COUNT):
		input_data = mutate_generic(input_data)
		print(input_data)
	exit(0)
