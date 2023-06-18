ascii_dict = {}

# Generate the dictionary
for char in range(ord('a'), ord('z') + 1):
    ascii_dict[chr(char)] = char

# Print the dictionary
print(ascii_dict)
