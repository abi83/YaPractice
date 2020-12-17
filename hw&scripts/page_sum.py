sum = 0

for i in range(1, 1000):
    sum += len(str(i))
    if sum == 1095:
        print(i, sum)

sum = 0
for i in range(1, 20):
    sum += i % 10 + i // 10 + i // 100
    print(sum)