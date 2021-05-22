n = int(input())
s = input()
count = 0
for char in s:
  if char == 'A':
    count += 1
  else:
    count -= 1
if count ==0:
  print("Friendship")
elif count>0:
  print("Anton")
else:
  print("Danik")
