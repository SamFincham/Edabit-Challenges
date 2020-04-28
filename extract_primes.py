#Create a function that takes an integer argument and returns a list of prime numbers found in the decimal #representation of that number.
#
#For example, extract_primes(1717) returns [7, 7, 17, 17, 71].
#
#The list should be in acending order. If a prime number appears more than once, every occurance should be #listed. If no prime numbers are found, return an empty list.

def extract_primes(n):
	n = str(n)
	
	#Get every possible number, filtering out "" and entries starting with "0" 
	all_num = [int(n[x:y]) for x in range(len(n)+1) for y in range(x, len(n)+1) if n[x:y] and n[x] != '0']

	#Select for prime only and return the sorted list
	return sorted([k for k in all_num if all([k%i for i in range(2,k)]) and k > 1])

print extract_primes(802300) #[]
print extract_primes(7) #[7]
print extract_primes(73) #[3, 7, 73]
print extract_primes(1313) #[3, 3, 13, 13, 31, 131, 313] 
