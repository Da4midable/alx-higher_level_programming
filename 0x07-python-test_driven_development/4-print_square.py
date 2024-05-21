#!/usr/bin/python3
def print_square(size):
	if size < 0:
		raise ValueError("size must be >= 0")
	if not isinstance(size, (int)):
		raise TypeError("size must be an integer")
	if not isinstance(size, float) and size < 0:
		raise TypeError("size must be an integer")
	if not size:
		raise TypeError("size cannot be empty")
	for x in range(0, size):
		[print("#", end="") for i in range(size)]
		print("")
	if size == 0:
		print("")
