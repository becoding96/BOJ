# 220725
l = ['*', ' ']

n = int(input())

if n == 1:
	print('*')
	exit()

for i in range(2 * n):
	for j in range(n):
		print(l[(i + j) % 2], end = '')
	print()