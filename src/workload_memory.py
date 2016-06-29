# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="apoorv"
__date__ ="$27 Jun, 2011 11:45:50 PM$"

UNIFORM = 0
import generate_code
from distributions import *
import matplotlib.pyplot as plt


if __name__ == "__main__":

	BLOCKS = 20
	AVG_MEM_JUMP = 100 #ints  PER BLOCK
	#FOR EACH BLOCK -
	AMPLITUDE = 20 #ints
	WRITE_PERCENT = 50
	DISTRIBUTION = UNIFORM # PROB OF ACCESSING A LOCATION IN RANGE
	ACCESSES = 100
	CONTINUOUS_BLOCKS = 20

	list_block_base = uniform( AVG_MEM_JUMP , BLOCKS)

	list_accesses   = []

	for base in list_block_base:
		list_accesses.append(code_distribution(base , AMPLITUDE , ACCESSES  , CONTINUOUS_BLOCKS ))

#create a linear list of accesses

	list_final_accesses = []
	max_loc = 0
	for block_list in list_accesses:
		for block in block_list:
			for element in block:
				if element> max_loc:
					max_loc = element
				list_final_accesses.append(element)


	list_functions = ['my_function']

	generate_code.standard_code()
	generate_code.code_from_accesses('my_function', list_final_accesses, max_loc, WRITE_PERCENT)
	generate_code.generate_main(list_functions)


	plt.plot(range(BLOCKS*ACCESSES), list_final_accesses)
	plt.axis([0, BLOCKS*ACCESSES , 0, max_loc + 100])
	plt.show()
