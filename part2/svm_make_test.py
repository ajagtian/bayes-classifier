#!/usr/bin/python3 -tt

import sys
import re
import os
import ast

def	get_file_text(filename):
		f = open(filename, 'rU', errors = 'ignore')
		text = f.read()
		f.close()
		text = text.replace('\n',' ')
		return text


def	hash_file(text):
		word_hash = {}
		words = re.findall(r'(\w+)', text)
		for word in words:
			if word.lower() not in word_hash.keys():
				word_hash[word.lower()] = 1
			else:
				word_hash[word.lower()] += 1
		return word_hash


def	convert_word_hash_to_id_hash(id_map, id, word_hash):
		id_hash = {}
		for word in word_hash.keys():
			if id_map.get(word):
				id_hash[id_map[word]] = word_hash[word]
			else:
				id_hash[id] =  word_hash[word]
				id += 1
		return (id_hash, id)


def	first_element(tuple):
		return tuple[0]


def	sort(id_hash):
		return sorted(id_hash, key=first_element)


def	append_to_file(out_file_handle, line):
		out_file_handle.write(line+'\n')		



def	format_id_hash_for_file_write(id_hash):
		text = str(0)
		for tuple in id_hash:
			text += ' '+str(tuple[0])+':'+str(tuple[1])
		
		return text


def	get_id_map():
		f = open('words', 'rU', errors = 'ignore')
		lines = f.readlines()
		id = int(lines[0][:-2])
		line1  = lines[1] 
		id_map = ast.literal_eval(line1)
		return (id_map, id)


def	read_testing_files(dir):
		filenames = os.listdir(dir)
		(id_map, id) = get_id_map()
		out_file_handle = open('svm_testing.txt', 'w')
		for filename in filenames:
			(id_hash, id) = convert_word_hash_to_id_hash(id_map, id+1, hash_file(get_file_text(os.path.join(dir, filename))))
			id_hash = sort(id_hash.items())
			append_to_file(out_file_handle, format_id_hash_for_file_write(id_hash))
		out_file_handle.close()


def main():
	args = sys.argv[1:]
	if(len(args) != 1):
		print('usage: ./svm_train.py <testing_dir>')
		sys.exit()

	read_testing_files(args[0])
		
		
		
if __name__ == '__main__':
	main()






		
		






