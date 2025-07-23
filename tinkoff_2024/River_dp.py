lr = input()
lr_list = []
for s in lr:
  lr_list.append(s)



dp_l = [0] * (len(lr_list) + 1)
dp_r = [0] * (len(lr_list) + 1)

dp_r[1] = 1


for i in range(2,len(lr_list)):
  print(i)
  r = min(dp_r[i - 1],dp_l[i] + 1)
  l = min(dp_l[i - 1],dp_r[i] + 1)
  if lr_list[i] == 'L':
    dp_l[i] = l
    dp_r[i] = r
  elif lr_list[i] == 'R':
    dp_l[i] = l
    dp_r[i] = r + 1
  elif lr_list[i] == 'B':
    dp_l[i] = l
    dp_r[i] = r
    
print(dp_l)
print(dp_r)
