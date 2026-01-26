# Given a string s of lowercase and uppercase English letters, the task is to find the first non-repeating character. If there is no such character, return '$'.

# Examples: 

# Input: s = "geeksForgeeks"
# Output: 'f'
# Explanation: 'f' is the first character in the string which does not repeat.

# Input: s = "Racecar"
# Output: 'e'
# Explanation: 'e' is the only character in the string which does not repeat.

# Input: "aabbccc"
# Output: '$'
# Explanation: All the characters in the given string are repeating.


def find_first_non_repeating_char(s: str) -> str:
	char_count = {}
	s = s.casefold()  # Normalize case to handle both lowercase and uppercase
	for char in s:
		if char in char_count:
			char_count[char] += 1
		else:
			char_count[char] = 1

	for char in s:
		if char_count[char] == 1:
			return char
	return '$'



print(find_first_non_repeating_char("aabbccc"))  # Output: '$'
print(find_first_non_repeating_char("geeksForgeeks"))  # Output: 'f
print(find_first_non_repeating_char("Racecar"))  # Output: 'e'