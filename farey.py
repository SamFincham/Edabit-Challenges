#The Farey sequence of order n is the set of all fractions with a denominator between 1 and n, reduced and #returned in ascending order. Given n, return the Farey sequence as a list, with each fraction being represented
#by a string in the form "numerator/denominator". 

def isvalid(a,b):
	return b >= a and all([b % i for i in range(2, a+1) if a % i == 0]) #Check if valid fraction

def farey(n):
	nd = [(x,y) for x in range(1,n+1) for y in range(1,n+1) if isvalid(x,y)] #Numerators and denomenators
	val = [p[0]/float(p[1]) for p in nd] #Values of fractions
	txt = ['%i/%i' % (p[0],p[1]) for p in nd] #Strings of fractions
	return ['0/1'] + [txt[q] for q in [val.index(p) for p in sorted(val)]]

print farey(3)
print farey(4)
print farey(5)
print farey(6)
print farey(7)
