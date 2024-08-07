def ERATOSPHEN(n):
    nums = []
    for n in range(0, n+1):
        nums.append(n)
    nums[0] = None
    nums[1] = None
    for n in nums:
        if n == None:
            continue
        for d in range(n*2,len(nums),n):
            nums[d] = None
    return list(filter(NoNone, nums))

def NoNone(num):
    return False if num == None else True

print(ERATOSPHEN(30))
