#!/usr/bin/python3 -tt

import re
import sys
import math

def	hash_line(line, global_hash, count_hash):
		"""tokenizes a line in training file"""
		sep = line.find(' ')
		clazz = line[:sep]
		hash = global_hash.get(clazz)
		clazz_count = count_hash.get(clazz)
		if not hash:
			hash = {}
			clazz_count = 0
		line = line[sep+1:]
		words = re.findall(r'(\w+)', line);
		for word in words:
			clazz_count += 1
			if word in hash.keys():
				hash[word] += 1
			else:
				hash[word] = 1

		global_hash[clazz] = hash
		count_hash[clazz] = clazz_count

		return (global_hash, count_hash)
		
		

def	hash_file(filename):
		f_handle = open(filename, 'rU', errors = 'ignore')
		## global_hash = hash of hashes, 
		## each key is a class and value if the word frequency map for that class
		global_hash = {}
		## count_hash = hash of total number of words in different classes
		count_hash = {}
		lines = f_handle.readlines()
		f_handle.close()
		## document_count = count of all the documents grouped by class
		document_count = {}
		for line in lines:
			clazz = line[:line.find(' ')]
			if clazz in document_count:
				document_count[clazz] += 1
			else:
				document_count[clazz] = 1
			(global_hash, count_hash) = hash_line(line, global_hash, count_hash)
		return (global_hash, count_hash, document_count)


def 	get_probabilities(global_hash, count_hash):
		g_hash1 = {}
		g_hash2 = {}
		for clazz in global_hash.keys():
			h1 = {}
			h2 = {}
			current_hash = global_hash[clazz]
			for word in current_hash.keys():
				h1[word] = math.log(current_hash[word] / count_hash[clazz], 10)
				h2[word] = math.log((current_hash[word]+1) / (count_hash[clazz] + len(current_hash)),10)
			g_hash1[clazz] = h1
			g_hash2[clazz] = h2
		return (g_hash1, g_hash2)


def	get_document_probabilities(document_count):
		document_probability = {}
		count = 0
		for document in document_count.keys():
			count += document_count[document]

		for document in document_count.keys():
			document_probability[document] = math.log(document_count[document] / count,10)
			
		return document_probability


def	generate_model_file(training_file_name, model_file):
		(global_hash, count_hash, document_count) = hash_file(training_file_name)
		model_file_handle = open(model_file, 'w', errors = 'ignore')
		(segment1, segment2) = get_probabilities(global_hash, count_hash)
		segment3 = get_document_probabilities(document_count)
		model_file_handle.write(str(segment1))
		model_file_handle.write('<<end_of_segment>>')
		model_file_handle.write(str(segment2))
		model_file_handle.write('<<end_of_segment>>')
		model_file_handle.write(str(segment3))
		model_file_handle.close()

def	main():
		args =	sys.argv[1:]
		if len(args) != 2:
			print('usage: ./nblearn.py <training_file> <model_file>')
			sys.exit(0)
		else:
			generate_model_file(args[0], args[1])
			

if __name__ == '__main__':
	main()
		
	
		

			
