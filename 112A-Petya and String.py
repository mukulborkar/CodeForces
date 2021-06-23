def compare(s1,s2):
  for i in range(len(s1)):
    if s1.lower()[i] < s2.lower()[i]:
      return -1
    elif s1.lower()[i] > s2.lower()[i]:
      return 1
  return 0
s1 = input()
s2 = input()
ans=compare(s1,s2)
print(ans)
