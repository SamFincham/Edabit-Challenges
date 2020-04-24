#For this exercise, keep in mind the following two terms (mutually exclusive):
#
#    initials = 1 character
#    words = 2+ characters (no dots allowed)
#
#A valid name is a name written in one of the following ways:
#
#    H. Wells
#    H. G. Wells
#    Herbert G. Wells
#    Herbert George Wells
#
#The following names are invalid:
#
#    Herbert or Wells (single names not allowed)
#    H Wells or H. G Wells (initials must end with dot)
#    h. Wells or H. wells or h. g. Wells (incorrect capitalization)
#    H. George Wells (middle name expanded, while first still left as initial)
#    H. G. W. (last name is not a word)
#    Herb. G. W. (dot only allowed after initial, not word)
#
#Rules
#
#    Both initials and words must be capitalized.
#    Initials must end with a dot.
#    A name must be either 2 or 3 words long (depending on whether a middle name exists).
#    If the name is 3 words long, you can expand the first and middle name or expand the first name only. #You cannot keep the first name as an initial and expand the middle name only.
#    The last name must be a word (not an initial).

def valid_name(name):
	#Identify elements of name
	nameok = True
	el = list()
	for x in name.split(" "):
		el.append(0) #0 = is invalid
		if x[0] == x[0].upper() and len(x) > 1:
			if len(x) == 2 and x[1] == '.':
				el[-1] = 1 #1 = Is initial
			elif x[1:-1] == x[1:-1].lower() and x.isalnum():
				el[-1] = 2 #2 = Is name

	#Check if OK
	if 0 in el: nameok = False
	if not 1 < len(el) < 4: nameok = False
	if el[-1] == 1: nameok = False
	if el[0] == 1 and el[1] == 2 and len(el) == 3: nameok = False
	
	return nameok

print valid_name("H. Wells")
print valid_name("H. G. Wells")
print valid_name("Herbert G. Wells")
print valid_name("Herbert")
print valid_name("h. Wells")
print valid_name("H Wells")
print valid_name("H. George Wells")
print valid_name("H. George W.")
