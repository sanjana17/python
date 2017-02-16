def fibonacci(n):
	if n == 0 or n == 1:
	   return n;
	else:
		return fibonacci(n-1)+fibonacci(n-2)

if __name__ == "__main__":
	i = int(input("enter a number "))
	print(fibonacci(i))
	
	# loop through range of numbers 
	# range(n) generates list of numbers starting from 0 to n-1 
	# eg: range(5) = [0, 1, 2, 3, 4]
	for n in range(5):
		print(n, fibonacci(n))
