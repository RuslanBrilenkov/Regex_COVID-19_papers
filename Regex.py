import re

# An example text to process
text = "Isabella is 16 years old, and Jonas is 24 years old. \
Their grandfather, Andrew, is 95 years old, and Andrew's father, Arthur, is 120."
# printing the text
print(text)

# Searching for the ages of people
ages = re.findall(r'\d{1,3}',text)
# printing the output
print("\n{}".format(ages))

# Searching for the names of people 
names = re.findall(r'[A-Z][a-z]+', text)
#names = re.findall(r"\b[A-Z][a-z]*", text1)
# printing the output
print("\n{}".format(names))

# Using a negative lookahead to exclude ownership form, such as Andrew's
names2 = re.findall(r'\b(?![A-Z][a-z]+\'s\b)[A-Z][a-z]+\b', text)
# printing the output
print("\n{}".format(names2))
