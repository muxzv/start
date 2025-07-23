lr = input()
lr_list = [0]
for s in lr:
  lr_list.append(s)

dp_l = [0] * (len(lr_list))
dp_r = [0] * (len(lr_list))

dp_r[0] = 1

for i in range(1,len(lr_list)):
  # print(i,lr_list[i])
  if lr_list[i] == 'L':
    dp_l[i] = min(dp_l[i - 1] + 1, dp_r[i - 1] + 1)
    dp_r[i] = min(dp_r[i - 1], dp_l[i - 1] + 1)
  elif lr_list[i] == 'R':
    dp_l[i] = min(dp_l[i - 1], dp_r[i - 1] + 1)
    dp_r[i] = min(dp_r[i - 1] + 1, dp_l[i - 1] + 1)
  elif lr_list[i] == 'B':
    dp_l[i] = min(dp_l[i - 1] + 1, dp_r[i - 1] + 2)
    dp_r[i] = min(dp_r[i - 1] + 1, dp_l[i - 1] + 2)
    
#print(dp_l)
#print(dp_r)

print(dp_r[-1])
