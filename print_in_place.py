# title: print_in_place.py

import time

for i in range(10):
	print(f'Counting: {i}', end='\r')
	time.sleep(1)
