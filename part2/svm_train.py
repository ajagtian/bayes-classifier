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


def	convert_word_hash_to_id_hash(id_map, word_hash):
		id_hash = {}
		for word in word_hash.keys():
			id_hash[id_map[word]] = word_hash[word]
		return id_hash


def	first_element(tuple):
		return tuple[0]


def	sort(id_hash):
		return sorted(id_hash, key=first_element)


def	append_to_file(out_file_handle, line):
		out_file_handle.write(line+'\n')		



def	format_id_hash_for_file_write(filename, id_hash, neg_class, pos_class):
		text = filename[:filename.find('.')]
		text = text.strip()
		neg_class = neg_class.strip()
		pos_class = pos_class.strip()
		if text == neg_class:
			text = str(-1)
		elif text == pos_class:
			text = str(1)
		else:
			text = str(0)

		for tuple in id_hash:
			text += ' '+str(tuple[0])+':'+str(tuple[1])
		
		return text


def	get_id_map():
		f = open('words', 'rU', errors = 'ignore')
		line1 = f.readlines()[1] 
		id_map = ast.literal_eval(line1)
		return id_map


def	read_training_files(dir, neg_class, pos_class):
		filenames = os.listdir(dir)
		id_map = get_id_map()
		out_file_handle = open('svm_training.txt', 'w')
		for filename in filenames:
			id_hash = sort(convert_word_hash_to_id_hash(id_map, hash_file(get_file_text(os.path.join(dir, filename)))).items())
			append_to_file(out_file_handle, format_id_hash_for_file_write(filename, id_hash, neg_class, pos_class))
		out_file_handle.close()


def main():
	args = sys.argv[1:]
	if(len(args) != 3):
		print('usage: ./svm_train.py <training_dir> <neg_class> <pos_class>')
		sys.exit()

	read_training_files(args[0], args[1], args[2])
		
		
		
if __name__ == '__main__':
	main()






		
		






