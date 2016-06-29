__author__="apoorv"
__date__ ="$27 Jun, 2011 11:46:27 PM$"

import random
import time, sys


"""
get 'count' uniformly distributed values in in 0 to amplitude
"""

def uniform(amplitude , count  ):
	set = []
	for i in range(count) :
		val = random.randint(0 , 2*amplitude-1 )
		set.append(val)

	return set

"""
get code distribution 'above' base value with amp = amplitude with
given no of continuous blocks and with access count =  count
"""

def code_distribution(base , amplitude , count , continuous_blocks):

	list_uniform_access = uniform(amplitude , count);
	list_uniform_access = sorted(list_uniform_access);

	block_size = count/continuous_blocks

	for i  in range( len(list_uniform_access) ):
		list_uniform_access[i] = list_uniform_access[i] + base

	#break list into blocks
	start = 0
	end = block_size
	list_sorted_blocks  = []

	for i in range(continuous_blocks):
		temp = list_uniform_access[start:end]
		list_sorted_blocks.append(temp)

		start = start + block_size
		end = end + block_size

	# now shuffle the blocks
	list_shuffled_blocks = []
	
	while True:
		size = len(list_sorted_blocks)
		rand_int = random.randint(0 , size-1)
		#put rand block into new list
		list_shuffled_blocks.append(list_sorted_blocks[rand_int])
		#remove the block from list
		list_sorted_blocks.remove(list_sorted_blocks[rand_int])
		if len(list_sorted_blocks) == 0:
			break

	return list_shuffled_blocks




