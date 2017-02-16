"""

update docstring

"""



def read_file(file_name):
	"""
	this function reads a file and prints out each line in the file
	accepts a file name string 
	returns None

	"""
	with open(file_name, "r") as input_file, open("output.txt", "w") as op:
		for line in input_file.readlines():
			words = line.split()
			for word in words:
				op.write(word+"\n")


def read_without_context_manager(file_name):
	file = open(file_name, "r")
	# read complete file at into a string
	file_content = file.read()
	print(file_content)

	for line in file.readlines():
		print(line)
	file.close()




if __name__ == "__main__":
	read_file("input.txt")
	read_without_context_manager("input.txt")