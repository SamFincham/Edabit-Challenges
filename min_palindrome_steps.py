#min_palindrome_steps
#
#Given an incomplete palindrome as a string, return the minimum letters needed to be added on to the end #to make the string a palindrome.

def min_palindrome_steps(txt):
	pal = txt; n = 0
	while pal != pal[::-1]:
		n += 1
		pal = txt + txt[::-1][-n:] #Merge txt and reverse txt, cut at n chars
	return n

print min_palindrome_steps("race")
print min_palindrome_steps("ah")
print min_palindrome_steps("mirror")
