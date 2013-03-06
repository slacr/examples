"""
An introductory example to Execnet
j bolton (boljay13)

Don't forget to add passphraseless ssh before running this:
$ ssh-agent bash
$ ssh-add

This program also requires a 'slacr.hosts' file to be present in the same directory
with a list of working hostnames.

This is a minimal example and doesn't provide any error checking.
"""

import execnet # Execnet libraries are on slacr-bifur

def sysinf(channel):
	import sys,os,socket 
	channel.send((socket.gethostname(), sys.version_info, os.getpid()))

def main():
	hosts = open("slacr.hosts")

	print("Creating execnet gateways to hosts in slacr.hosts file..")
	"""
	Loop through every line in the file, passing each as a hostname to execnet.makegateway()
	Note: you must strip off the newline character (\n) for every host (I used rstrip())
	"""
	gws = [execnet.makegateway("ssh="+h.rstrip()) for h in hosts]
	print("Remotely executing a function on each host...")
	cs =  [gw.remote_exec(sysinf) for gw in gws]
	print("Receiving back system information for each host...")
	inf = [c.receive() for c in cs]
	print(inf)

if __name__ == "__main__":
	main()
