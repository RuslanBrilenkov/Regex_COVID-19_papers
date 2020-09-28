import re


text1 = "Isabella is 16 years old, and Jonas is 24 years old. \
Their grandfather, Andrew, is 95 years old, and Andrew's father, Arthur, is 120."

print(text1)

names = re.findall(r'[A-Z][a-z]+', text1)
#names = re.findall(r"\b[A-Z][a-z]*", text1)

print()
print(names)

ages = re.findall(r'\d{1,3}',text1)

print()
print(ages)
