#!/usr/bin/python3 -tt


import sys

def	convert_file(in_filename, out_filename, neg_class, pos_class):
		f1 = open(in_filename, 'rU', errors = 'ignore')
		f2 = open(out_filename, 'w')
		lines = f1.readlines()
		f1.close()
		for line in lines:
			if line[0] == '-':
				f2.write(neg_class+'\n')
			else:
				f2.write(pos_class+'\n')
		f2.close()



def	main():
		args = sys.argv[1:]	
		if len(args) != 4:
			print('usage: ./convert_svm_to_binary_results <from_file> <to_file> <neg_class> <pos_class>')
			sys.exit(0)	
		convert_file(args[0], args[1], args[2], args[3])


if __name__  == '__main__':
	main()

