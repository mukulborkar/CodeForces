s = input()
clower = 0
cupper = 0
for char in s:
  if char.islower():
    clower += 1
  else:
    cupper += 1
if clower >= cupper:
  print(s.lower())
else:
  print(s.upper())
