#!/usr/bin/python3 -tt

import sys
import re
import math
import ast

def	modelfile_to_hash(model_filename):
		model_file_handle = open(model_filename, 'rU', errors = 'ignore')
		text = model_file_handle.read()
		segments = text.split('<<end_of_segment>>')
		probability_hash  = ast.literal_eval(segments[0])
		smoothed_hash = ast.literal_eval(segments[1])
		document_probability = ast.literal_eval(segments[2])
		print(probability_hash, smoothed_hash, document_probability)
		return (probability_hash, smoothed_hash, document_probability)


def	main():
		args = sys.argv[1:]
		if(len(args) != 1):
			print('usage: ./nbclassify <model_file> <test_file> <output_file>')
			sys.exit(0)
		
		modelfile_to_hash(args[0])



if __name__ == '__main__':
	main()
