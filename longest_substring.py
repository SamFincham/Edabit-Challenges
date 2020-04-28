#Given a string of digits, return the longest substring with alternating odd/even or even/odd digits. If two #or more substrings have the same length, return the substring that occurs first.

def longest_substring(digits):
	seq = list(); txt = '' #Important variables
	digits = [(k, int(k)%2 == 0) for k in list(digits)] #Convert to list of integers and if even/odd

	#Chop into strings of alternating odd-even
	for k in range(1, len(digits)):
		if digits[k][1] != digits[k-1][1]:
			if not txt:
				txt += digits[k-1][0]
			txt += digits[k][0]
		elif txt:
			seq.append(txt)
			txt = ''
	if txt: seq.append(txt)

	#Return the first largest
	le = max(len(k) for k in seq)
	for k in seq:
		if len(k) == le: return k

print longest_substring("225424272163254474441338664823") #272163254
print longest_substring("594127169973391692147228678476") #16921472
print longest_substring("721449827599186159274227324466") #7214
