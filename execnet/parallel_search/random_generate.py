"""
Randomly generate a crapload of numbers
"""

import random

if __name__ == "__main__":
	f = open('numbers','w')
	random.seed()
	for i in range(1000000):
		f.write(str(round(random.uniform(1,1000000))) + '\n')
