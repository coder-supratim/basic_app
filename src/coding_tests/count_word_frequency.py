def findWordFrequency (text) :
	words = text.lower().split()
	freq = dict()
	
	for word in words:
		if word in freq:
			freq[word] += 1
		else:
			freq[word] = 1
	return freq


# Shorter version using dict.get() method
def shortWordFrequency(text):
	words = text.lower().split()
	freq = {}

	for word in words:
		freq[word] = freq.get(word,0) +1 
	return freq
print(shortWordFrequency("The gpt is a powerful language model that can generate human-like text. The gpt is widely used in natural language processing tasks."))
print(findWordFrequency("The quick brown fox jumps over the lazy dog"))