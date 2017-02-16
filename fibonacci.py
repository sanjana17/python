i = int(raw_input("enter a number "));
def fibonacci(n):
	if n==0 or n==1:
	   return n;
	else:
		return fibonacci(n-1)+fibonacci(n-2);

a = fibonacci(i);
print a;