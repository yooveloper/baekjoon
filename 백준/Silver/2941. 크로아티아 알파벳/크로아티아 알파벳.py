croatia = ("c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z=")
s = input()

for c in croatia:
    s = s.replace(c, "*")

print(len(s))