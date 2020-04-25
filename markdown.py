#Complete the function "markdown" so that it takes in a symbol as input, and returns a function which #applies that formatting to a given word in a given sentence.

def markdown(symb):
	def format_txt(txt, s):
		ans = ''
		for x in txt.split():
			if x.lower().find(s.lower()) != -1:
				x = symb + x + symb
			ans += x + ' '
		return ans[:-1]
	return format_txt

italicise = markdown('*')
print italicise('Hello there!', 'Hello')
print italicise('The tale of the two sparrows', 'the')
print italicise('Include punctuation!', 'punctuation')

inline = markdown('`')
print inline('Remember to return a boolean value', 'boolean')
print inline('I want you to create the class Programmer...', 'PROGRAMMER')
print inline('DO not forget to return the value', 'return')
