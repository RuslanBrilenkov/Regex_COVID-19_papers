import re

# An example text to process
text = "Isabella is 16 years old, and Jonas is 24 years old. \
Their grandfather, Andrew, is 95 years old, and Andrew's father, Arthur, is 120."
# printing the text
print(text)

# Searching for the names of people 
names = re.findall(r'[A-Z][a-z]+', text1)
#names = re.findall(r"\b[A-Z][a-z]*", text1)
# printing the output
print("\n{}".format(names))

# Searching for the ages of people
ages = re.findall(r'\d{1,3}',text1)
# printing the output
print("\n{}".format(ages))
