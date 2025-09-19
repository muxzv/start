l = [10,9,10,9]#list(map(int,input().split()))
on = l[0]
off = l[1]
first = l[2]
second = l[3]

if on == off == first == second:
    print('Both')
elif first == on and second == off:
    print('First')
elif first == off and second == on:
    print('Second')
else:
    print('None')
