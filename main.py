

from generic_mutator import *

if __name__=="__main__":
	input_data = ""
	COUNT = 100000
	for _ in range(COUNT):
		mutate_generic(input_data)
		#print(input_data)
	exit(0)
