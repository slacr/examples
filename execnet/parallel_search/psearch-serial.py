#!/usr/bin/env python3

# The execnet serial searching program from http://slacr.evergreen.edu/wiki/index.php/Execnet_Parallel_Search
# made to help beginners learning execnet


import sys

def readlines(filename):
	try:
		lines = [x.strip() for x in open(filename)]
		return lines
	except IOError as strerror:
		print("I/O error: " + str(strerror))
	except ValueError:
		print("Could not parse data in file as string(s)")
	except:
		print("Unexpected error:", sys.exc_info()[0])
		raise

def search(target, domain):
	found = []
	for i in range(len(domain)):
		if domain[i] == target:
			found.append(i)
	return found

def main(argv):
	target = argv[0]
	domain_file = argv[1]
	domain = readlines(domain_file)
	indices = search(target, domain)
	print("Target",target,"found at indices",indices)

def usage():
	print("Usage:")
	print("python3 psearch.py <target value> <domain file>")
	print("e.g.:   python3 psearch.py 99 /home/osl/tony/numbers.txt")

if __name__ == "__main__":
	if len(sys.argv) != 3: usage()
	else: main(sys.argv[1:])

