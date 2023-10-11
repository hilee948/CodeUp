m = []
for i in range(10):
  m.append(list(map(int, input().split())))

cur_pos = [1,1]
while 1:
  x=cur_pos[0]
  y=cur_pos[1]
  cur_val = m[x][y]
  if cur_val == 2:
    m[x][y] = 9
    break
  elif cur_val == 0:
    m[x][y] = 9
    #check right
    if m[x][y+1] == 0 or m[x][y+1] == 2:
      cur_pos = [x,y+1]
    else:
      #check bottom
      if m[x+1][y] == 0 or m[x+1][y] == 2:
        cur_pos = [x+1,y]
      else:
        break
  else:
    break

for i in range(10):
  for j in range(10):
    print(m[i][j], end=' ')
  print()
