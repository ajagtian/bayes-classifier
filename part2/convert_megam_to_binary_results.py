#!/usr/bin/python3 -tt


import sys

def	convert(old_file, new_file, pos, neg):
		f = open(old_file, 'rU', errors = 'ignore')
		lines = f.readlines()
		f.close()
		lines_out = []
		for line in lines:
			clazz = line[:1]
			if clazz  == '0':
				lines_out.append(neg+'\n')
			else:
				lines_out.append(pos+'\n')
			
		
		f = open(new_file, 'w')
		f.writelines(lines_out)
		f.close()


def	main():	
		args= sys.argv[1:]
		if len(args) != 4:
			print('usage: ./convert_megam_to_binary_results <raw_file> <out_file> <pos_class> <neg_class>')
			sys.exit(0)
		
		convert(args[0], args[1], args[2], args[3])


if __name__ == '__main__':
	main()
		
			
