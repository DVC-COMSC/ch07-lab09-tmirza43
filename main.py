# ******************************
# Make your Code
# ******************************

names = []
shortest = ''
longest = ''

for i in range(5):
  name = str(input("Enter a name: "))
  names.append(name)
  if i == 0:
    shortest = name
  elif len(name) == len(shortest):
    if ord(name[0]) < ord(shortest[0]):
      shortest = name
  if len(name) > len(longest):
    longest = name
  if len(name) < len(shortest):
    shortest = name
      
print(shortest, longest)