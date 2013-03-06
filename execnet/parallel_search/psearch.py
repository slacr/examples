#!/usr/bin/env python3

# The execnet parallel searching program from http://slacr.evergreen.edu/wiki/index.php/Execnet_Parallel_Search
# made to help beginners learning execnet

import execnet, sys

HOSTS_FILE = 'slacr.hosts'

def create_group(hostfile):
	hosts = ["ssh=" + h for h in readlines(hostfile)]
	gateways = []
	for h in hosts:
		try:
			gateways.append(execnet.makegateway(h))
			print("node {0} connected".format(h))
		except: 
			print("Could not open gateway:", sys.exc_info()[0])
	return gateways

def master(gateways, t, d):
	parted = partition(d, round(len(d)/len(gateways)))
	node_data = zip(gateways, list(parted))
	channels,result = [],[]
	for node, data in node_data:
		channels.append(node.remote_exec(search, target=t, domain=data))
	for c in channels: 
		result += c.receive()
	return result

def partition(ls, n):
	for i in range(0, len(ls), n):
		yield ls[i:i+n]

def usage():
	print("Usage:")
	print("python3 psearch.py <target value> <domain file>")
	print("e.g.:   python3 psearch.py 99 /home/osl/tony/numbers.txt")

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

def search(channel, target, domain):
	found = []
	for i in range(len(domain)):
		if domain[i] == target:
			found.append(i)
	channel.send(found)

def main(argv):
	target = argv[0]
	domain_file = argv[1]
	domain = readlines(domain_file)
	group = create_group(HOSTS_FILE)
	indices = master(group, target, domain)
	print("Target",target,"found at indices",indices)

if __name__ == "__main__":
	if len(sys.argv) != 3: usage()
	else: main(sys.argv[1:])

