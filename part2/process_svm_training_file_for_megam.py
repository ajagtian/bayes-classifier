#!/usr/bin/python3 -tt

import sys


def	convert(training_filename, new_training_filename, pos_class, neg_class):
		f = open(training_filename, 'rU',errors = 'ignore')
		lines = f.readlines();
		f.close()
		lines_out= []
		for line in lines:
			clazz = line[:line.find(' ')]
			if clazz == pos_class:
				clazz = str(1)
			else:
				clazz = str(0)
			lines_out.append(clazz+' '+line[line.find(' ')+1:])	
		
		f_out = open(new_training_filename, 'w')
		f_out.writelines(lines_out)
		f_out.close()


def	main():
		args = sys.argv[1:]
		if len(args) != 4:
			print('usage: ./process_training_file_for_megam <source_file> <dest_file> <pos_class> <neg_class>')
			sys.exit(0)
		
		convert(args[0], args[1], args[2], args[3])


if __name__ == '__main__':
	main()		
