#A left-truncatable prime is a prime number that contains no 0 digits and, when the first digit is #successively removed, the result is always prime.
#
#A right-truncatable prime is a prime number that contains no 0 digits and, when the last digit is #successively removed, the result is always prime.
#
#Create a function that takes an integer as an argument and:
#
#    If the integer is only a left-truncatable prime, return "left".
#    If the integer is only a right-truncatable prime, return "right".
#    If the integer is both, return "both".
#    Otherwise, return False.

def truncatable(n):
	def isprime(a):
		return all([a%i for i in range(2, a)]) and a > 1

	n = str(n)
	if n.find("0") != -1: return False

	left = all([isprime(int(n[i:])) for i in range(0, len(n)) if n[i:]])
	rght = all([isprime(int(n[:-i])) for i in range(0, len(n)) if n[:-i]])
		
	return {(True, False): 'left', (False, True): 'right', (True, True): 'both'}.get((left, rght), False)

print truncatable(9137) #left
print truncatable(5939) #right
print truncatable(317) #both
print truncatable(5) #both
print truncatable(139) #False
print truncatable(103) #False

