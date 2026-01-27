# Question: Reverse a string without using built-in reverse functions. 


def reverse_string (s: str) -> str:
	# reversed_string = s[::-1] # Easy but incorrect implementation using slicing

	reversed_string = ""
	for char in s:
		reversed_string = char + reversed_string
		print(reversed_string)  # Debug: Show intermediate reversed string state
	return reversed_string

print(reverse_string("reversed"))
