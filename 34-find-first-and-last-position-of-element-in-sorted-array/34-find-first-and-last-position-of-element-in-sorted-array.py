f = open("user.out", 'w')
for nums, tar in zip(stdin, stdin):
    if nums[1] == ']':
        print("[-1,-1]", file=f)
        continue
    a = nums[1:-2].split(',')
    tar = tar.rstrip()
    t = int(tar)
    i = bisect_left(a, True, key=lambda x: int(x) >= t)
    if i == len(a) or a[i] != tar:
        print("[-1,-1]", file=f)
    else:
        j = bisect_left(a, True, key=lambda x: int(x) > t)
        print(f"[{i},{j-1}]", file=f)
exit(0)