#!/usr/bin/python3 -tt

import sys

def	traverse(in_lines, out_lines, clazz):
		correct_guess = 0
		total_guess = 0
		total_count = 0
		for i in range(len(in_lines)):	
			if in_lines[i].strip()== clazz:
				total_count += 1
			if out_lines[i].strip() == clazz:
				total_guess += 1
			if out_lines[i].strip() == clazz and in_lines[i].strip() == clazz:
				correct_guess += 1
		return (correct_guess, total_guess, total_count)

def	precision(correct_guess, total_guess):
		return correct_guess / total_guess


def	recall(correct_guess, total_count):
		return correct_guess / total_count


def	f_score(precision, recall):
		return (2 * precision * recall) / (precision +  recall)


def	lines(filename):
		f = open(filename, 'rU', errors = 'ignore')
		lines = f.readlines()
		f.close()
		return lines


def	main():
		args = sys.argv[1:]
		if len(args) != 3:
			print('usage: ./f_score <in_file> <out_file> <class>')	
			sys.exit(0)

		(correct_guess, total_guess, total_count) = traverse(lines(args[0]), lines(args[1]), args[2])
		score = f_score(precision(correct_guess, total_guess), recall(correct_guess, total_guess))
		print(score)


if __name__ == '__main__':
	main()
		

		
		



	
			
					
