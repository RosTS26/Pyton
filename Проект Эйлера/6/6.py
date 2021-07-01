
sqr = 0
b = 0

for a in range(1, 101):
	A = a ** 2
	sqr += A
	b += a

B = b ** 2

print(B)
print(sqr)

al = B - sqr

print(al)