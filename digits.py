#Imagine you took all the numbers between 0 and n and concatenated them together into a long string. How many #digits are there between 0 and n? Write a function that can calculate this.
#
#There are 0 digits between 0 and 1, there are 9 digits between 0 and 10 and there are 189 digits between 0 and #100.

def digits(n):
	d = len(str(n))
	ans = (n - 10**(d-1))*d #Digits with length d
	for x in range(1, d): #Digits with length d-1, d-2, etc.
		ans += (10**x - 10**(x-1))*x

	return ans

print digits(1) #0
print digits(10) #9
print digits(100) #189
print digits(2020) #6969
