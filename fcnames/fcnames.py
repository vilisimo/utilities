"""
Script that parses python files to produce class & function names.
Originally used for parsing the names of tests for master's thesis.
Note that only classes and functions belonging to them are parsed.

To do: 
	1. Functions without classes. 
	2. Inner classes & their methods.
	3. Ask user for a path
	4. Ask user for an output path
"""

def nameParser(input_file):
	output = []
	with open(input_file) as f:
		for line in f:
			line = line.strip()
			if line.startswith('class'):
				output.append(line)
			if line.startswith('def') and 'setUp' not in line:
				line = line.split('def')
				output.append('\t' + line[1])
	print("Reading is done!")
	return output

def nameWriter(output_file, material):
	with open(output_file, 'w') as f:
		for line in material:
			line = line + '\n'
			f.write(line)
	print("Writing is done!")


if __name__ == "__main__":
	path = '/Users/vilisimo/project/pimp/django_projects/pimp/grouping/'
	name = 'tests.py'
	input_file = path + name
	material = nameParser(input_file)

	output_file = 'output.txt'
	nameWriter(output_file, material)