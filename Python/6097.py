h,w = map(int, input().split())
n = int(input())
st = []
for i in range(n):
  st.append(list(map(int, input().split())))

p = [[0]*w for _ in range(h)]

for i in range(n):
  x = st[i][2]-1
  y = st[i][3]-1
  d = st[i][1]
  l = st[i][0]
  if d==0:
    for j in range(l):
      p[x][y+j] = 1

  elif d==1:
    for j in range(l):
      p[x+j][y] = 1

for i in range(h):
  for j in range(w):
    print(p[i][j], end=' ')
  print()
