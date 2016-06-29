import random
__author__="apoorv"
__date__ ="$29 Jun, 2011 8:15:58 PM$"

def standard_code():
	print "#include <stdio.h>"
	print "#include <stdlib.h>"



#puts the code in proper format and prints on the standard output
def generate_main(list_functions):
	print "int main(){"
	for function in list_functions:
		print function , "();"
	print '}'




#INPUTS-
#function_name - obvious
#list_accesses - list of memory accesses by the function
#max_loc - maximum location accessed , used to allocate memory chunk
#write_percent - obvious

#OUTPUT
#prints the function on standard output
#redirect to a file
def code_from_accesses(function_name , list_accesses , max_loc , write_percent):
	print 'void' , function_name , "(){"
	print "//max_loc - " , max_loc
	print "//write percent - " , write_percent
	print "int i; // for reads"
	print "int* heap = (int*)malloc(" , max_loc+1 , "*sizeof(int) );"

	for access in list_accesses:
		rand_int = random.randint(1 , 100)
		if rand_int <= write_percent:
			print "heap[" , access  , "] = "  , rand_int , ';'
		else:
			print "i = heap[" , access  , "]; "
	print "}"
