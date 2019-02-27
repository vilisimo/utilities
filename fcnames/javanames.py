"""
Script that parses java file and produces test method names.
"""

import sys

def nameParser(input_file):
	output = []
	with open(input_file) as f:
		for line in f:
			line = line.strip()
			if line.startswith('public void'):
				line = line.split('public void')[1]
				line = line.split('()')
				output.append('\t' + line[0])
	print("Reading is done!")
	return output

def nameWriter(output_file, material):
	with open(output_file, 'w') as f:
		for line in material:
			line = line + '\n'
			f.write(line)
	print("Writing is done!")


if __name__ == "__main__":
	path = sys.argv[1]
	material = nameParser(path)

	output_file = 'output.txt'
	nameWriter(output_file, material)