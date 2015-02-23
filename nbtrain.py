#!/usr/bin/python3 -tt

import sys
import os

def	readfile(filename):
		"""reads a input file and returns as single line text"""
	
		f = open(filename, 'rU', errors = 'ignore')
		text =f.read()
		f.close()
		return text.replace('\n',' ').replace('\r','');


def	create_training_file(dir, dest_file, option):
		"""creates a training file from a list of files, 
		this training file can then be used for NB learning"""
		
		filenames = sorted(os.listdir(dir))
		out_file_handle  = open(dest_file, 'w')
		lines = []
		for file in filenames:
			filetext = readfile(os.path.join(dir, file))
			lines = append_to_file(file, filetext, lines, option)
		out_file_handle.writelines(lines)
		out_file_handle.close()


def	append_to_file(filename, filetext, lines, option):
		"""appends a line to the training file"""
		if option == '-train':
			lines.append(filename[:filename.find('.')]+' '+filetext+'\n')		
		if option == '-test':
			lines.append(filetext+'\n')
	
		return lines
		

def	main():
		args = sys.argv[1:]
		if len(args) < 2:
			print('usage: ./nbtrain.py [-test|-train] <source_directory> <training_file_name>')
			sys.exit(0)
		if len(args) == 2:
			create_training_file(args[0], args[1], '-train')
		else:
			option = args[0]
			create_training_file(args[1], args[2], option)
		

if __name__ == '__main__':
	main()	
