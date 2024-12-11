f = open('input.txt', 'r')
nums = [int(x) for x in f.read().split()]
summa = 0

for i in range(25):
    print(i)
    ans = []

    for x in nums:
        l = len(str(x))

        if x == 0:
            ans.append(1)
        elif l % 2 > 0:
            ans.append(x * 2024)
        else:
            ans.append(int(str(x)[:l // 2]))
            ans.append(int(str(x)[l // 2:]))

    nums = ans

print(len(nums))
