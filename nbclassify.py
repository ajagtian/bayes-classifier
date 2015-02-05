#!/usr/bin/python3 -tt

import sys
import re
import ast


def	modelfile_to_hash(model_filename):
		model_file_handle = open(model_filename, 'rU', errors = 'ignore')
		text = model_file_handle.read()
		segments = text.split('<<end_of_segment>>')
		probability_hash  = ast.literal_eval(segments[0])
		smoothed_hash = ast.literal_eval(segments[1])
		document_probability = ast.literal_eval(segments[2])
		return (probability_hash, smoothed_hash, document_probability)


def	vocab(line):	
		return re.findall(r'(\w+)', line)


def	need_smoothing(line_vocab, document):
		for word in line_vocab:
			word = word.lower()
			if document.get(word):
				continue
			else:
				return True
		return False


def	second_element(tuple):
		return tuple[1]


def	get_lines(test_file_name):
		f = open(test_file_name, 'rU', errors = 'ignore')
		lines = f.readlines()
		f.close()
		return lines


def	classify_lines(filelines, probability_hash, smoothed_hash, document_probability):
		classes = ''
		for line in filelines:
			classes += classify_line(line, probability_hash,smoothed_hash, document_probability).strip() + '\n'
		return classes

	
def	classify_line(line, prob_hash, smoothed_hash, doc_prob):
		words = vocab(line)
		needs_smoothing = need_smoothing(words, prob_hash)
		if needs_smoothing:
			clazz = classify_line_(line, smoothed_hash, doc_prob)
		else:
			clazz = classify_line_(line, prob_hash, doc_prob)

		return clazz

			
def	classify_line_(line, hash, doc_prob):
		prob = {}
		for clazz in hash.keys():
			current_probs = hash[clazz]
			prob[clazz] = 0
			for word in vocab(line):
				word = word.lower()
				if current_probs.get(word):
					prob[clazz] += current_probs[word]
				else:
					prob[clazz] += current_probs['zero']
			prob[clazz] += doc_prob[clazz]
		return sorted(prob.items(), reverse=True, key=second_element)[0][0]
				
				
def	main():
		args = sys.argv[1:]
		if(len(args) != 2):
			print('usage: ./nbclassify <model_file> <test_file>')
			sys.exit(0)
		(probability_hash, smoothed_hash, document_probability) = modelfile_to_hash(args[0])
		lines = get_lines(args[1])
		classes = classify_lines(lines, probability_hash, smoothed_hash, document_probability)
		print(classes[:-1])
		f = open(args[0][:-2]+'out', 'w')
		f.write(classes)
		f.close()		
		

if __name__ == '__main__':
	main()
