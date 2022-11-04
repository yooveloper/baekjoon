all = set(i for i in range(1, 10001)) # {1,2,3 ...9999,10000}
s = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    s.add(i)
    
for i in sorted(all - s):
    print(i)
