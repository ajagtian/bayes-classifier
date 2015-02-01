#!/usr/bin/python3 -tt


import sys

def	extract_class_from_line(line):
		return line[:line.find(' ')]


def	extract_class_from_lines(lines):
		classes = ''
		for line in lines:
			classes += extract_class_from_line(line)+'\n'
		return classes


def	write_file_with_text(text, filename):
		f = open(filename, 'w')
		f.write(text)
		f.close()

def	get_file_lines(filename):
		f = open(filename, 'rU', errors = 'ignore')
		lines = f.readlines()
		f.close()
		return lines


def	main():
		args = sys.argv[1:]
		if len(args) != 2:
			print('usage: ./extract_training_classes <from_file> <to_file>')
			sys.exit(0)
		lines = get_file_lines(args[0])
		text = extract_class_from_lines(lines)
		write_file_with_text(text, args[1])


if __name__ == '__main__':
	main()
				
		
		
		

