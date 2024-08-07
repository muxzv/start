def ERATOSPHEN(n):
    nums = []
    for n in range(0, n+1):
        nums.append(True)
    nums[0] = False
    nums[1] = False
    #print(nums)
    for n in range(len(nums)):
        if nums[n] == False:
            continue
        for d in range(n*2,len(nums),n):
            nums[d] = False
    #print(nums)
    r = []
    for i, e in enumerate(nums):
        if e:
            r.append(i)
    return r

print(ERATOSPHEN(30))
