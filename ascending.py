#Write a function that returns True if a string consists of ascending AND consecutive numbers.

def ascending(txt):
	for d in range(1,len(txt)):
		n = [int(txt[k:(k+d)]) for k in range(0, len(txt), d)]
		if all([(n[a] == n[a-1]+1) for a in range(1,len(n))]):
			return True
			
	return False

print ascending("232425") #True: 23, 24, 25
print ascending("2324256") #False
print ascending("444445") #True: 444, 445
