def read_file(file_name):
	with open(file_name, "r") as input_file, open("output.txt", "w") as op:
		for line in input_file.readlines():
			words = line.split()
			for word in words:
				op.write(word+"\n")


def read_without_with(file_name):
	file = open(file_name, "r")
	# read complete file at into a string
	file_content = file.read()
	print(file_content)

	for line in file.readlines():
		print(line)
	file.close()




if __name__ == "__main__":
	read_without_with("input.txt")