m=[]
for i in range(7):
  m.append(list(map(int, input().split())))
c = [[0]*7 for _ in range(7)]
boom = 0

def dfs(x,y,n):
  if x<0 or y<0 or x>=7 or y>=7:
    return 0
  if c[x][y]==0 and m[x][y]==n:
    c[x][y]=1
    cnt = 1+dfs(x-1,y,n)+dfs(x+1,y,n)+dfs(x,y-1,n)+dfs(x,y+1,n)
    return cnt
  return 0

for i in range(7):
  for j in range(7):
    if c[i][j]==0:
      cnt = dfs(i,j,m[i][j])
      if cnt>=3:
        boom+=1
print(boom)
