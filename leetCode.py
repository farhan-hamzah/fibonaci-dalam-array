n = int(input())
x = int(input())
y = int(input())
hasil = [x, y]
for i in range(2, n):
    p = (hasil[-1] + hasil[-2])
    hasil.append(p)
print(hasil)
