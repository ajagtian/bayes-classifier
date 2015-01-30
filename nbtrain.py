#!/usr/bin/python3 -tt

import sys
import os

def	readfile(filename):
		"""reads a input file and returns as single line text"""
	
		f = open(filename, 'rU', errors = 'ignore')
		text =f.read()
		f.close()
		return text.replace('\n',' ');


def	create_training_file(dir, dest_file):
		"""creates a training file from a list of files, 
		this training file can then be used for NB learning"""
		
		filenames = os.listdir(dir)
		out_file_handle  = open(dest_file, 'w')
		for file in filenames:
			filetext = readfile(os.path.join(dir, file))
			append_to_file(out_file_handle, file, filetext)
		out_file_handle.close()


def	append_to_file(filehandle, filename, filetext):
		"""appends a line to the training file"""

		filehandle.write(filename[:filename.find('.')]+' '+filetext+'\n')		
		## to create a test file, uncomment following line, and comment the above one
		##filehandle.write(filetext+'\n')
		

def	main():
		args = sys.argv[1:]
		if len(args) != 2:
			print('usage: ./nbtrain.py <source_directory> <training_file_name>')
			sys.exit(0)
		create_training_file(args[0], args[1])
		

if __name__ == '__main__':
	main()	
