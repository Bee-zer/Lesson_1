i = 457495747
ls = []
while i > 10:
    ls.append(i % 10)
    i //= 10
r = max(ls)
print(r)