#!/usr/bin/python3 -tt

import sys

def	read(filename):
		f = open(filename, 'rU', errors = 'ignore')
		lines = f.readlines()
		f.close()
		classes = []
		line_n = 0
		for line in lines:
			line_n += 1
			clazz = line[:4]
			if clazz not in classes:
				if(clazz == 'ha -' or clazz == 'spa ' or clazz == 'ha  ' or clazz == 'lis '):

					classes.append(clazz+' '+str(line_n))
				else:
					classes.append(clazz)
		print (classes, line_n)

def	main():
		read(sys.argv[1])


if __name__ == '__main__':
	main()
		
