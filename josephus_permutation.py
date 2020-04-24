""" Josephus Permutation """

#A group of n prisoners stand in a circle awaiting execution. Starting from an arbitrary position(0), the #executioner kills every kth person until one person remains standing, who is then granted freedom (see #examples).

#Create a function that takes 2 arguments - the number of people to be executed (n) and the step size (k), and returns the original position (index) of the person who survives.

def who_goes_free(n, k):
	p = range(0,n) #Prisoners
	while len(p) > 1:
		dn = (k-1)%len(p) #Death Number
		p = p[(dn+1):] + p[:dn] #Execute Prisoner at index dn and rearrange

	return p[0]

print who_goes_free(9,2)
print who_goes_free(9,3)
