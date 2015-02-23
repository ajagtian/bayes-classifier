#!/usr/bin/python3 -tt

import sys
import re
import os

def	index_file(filename, global_word_hash, id):
		f = open(filename, 'rU', errors = 'ignore')
		text = f.read()
		words = re.findall(r'(\w+)', text)
		
		for word in words:
			if word.lower() not in global_word_hash.keys():
				global_word_hash[word.lower()] = id
				id += 1
		return (global_word_hash, id)


def	index_files(dir):
		filenames = os.listdir(dir)
		id = 1
		global_word_hash = {}
		for filename in filenames:
			(global_word_hash, id) = index_file(os.path.join(dir, filename), global_word_hash, id)
		
		return (global_word_hash, id)


def 	write_word_hash_file(id, global_word_hash, words_file_name):
		f = open(words_file_name, 'w')
		f.write(str(id-1)+'\n'+str(global_word_hash))
		f.close()


def	main():
		args = sys.argv[1:]
		if(len(args) != 2):
			print('usage: ./index_words <training_directory> <words_file_name>')
			sys.exit(0)
		(global_word_hash, id) = index_files(args[0])
		write_word_hash_file(id, global_word_hash, args[1])


if __name__ == '__main__':
	main()
				







		

		
				
