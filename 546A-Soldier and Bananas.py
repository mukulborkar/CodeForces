k,n,w = map(int,input().split())
ans = 0
for i in range(1,w+1):
  ans += k*i
if ans <= n:
  print(0)
else:
  print(ans-n)

