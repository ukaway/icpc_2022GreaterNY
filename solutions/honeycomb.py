# m: width
# n: height
# c: number of common walls shared by hexagonal cells
# c(2, n) = 1, 3, 6, 8, 11, 13... = m-1, (-2m+2)+(6m-7), (m-1)+(6m-7), (-2m+2)+2(6m-7), (m-1)+2(6m-7)...
# c(2, n+1) - c(2, n) = 2, 3, 2, 3... = 3m-4, 3m-3, 3m-4...
# c(3, n) = 2, 7, 13, 18, 24, 30... = m-1, (-2m+2)+(6m-7), (m-1)+(6m-7), (-2m+2)+2(6m-7), (m-1)+2(6m-7)...
# c(3, n+1) - c(3, n) = 5, 6, 5, 6... = 3m-4, 3m-3, 3m-4...
# c(4, n) = 3, 11, 20, 28, 37, 45... = m-1, (-2m+2)+(6m-7), (m-1)+(6m-7), (-2m+2)+2(6m-7), (m-1)+2(6m-7)...
# c(4, n+1) - c(4, n) = 8, 9, 8, 9... = 3m-4, 3m-3, 3m-4...

[m, n] = [int(x) for x in input().split()]
cell = m*n - n//2
if n % 2 == 0:
    c = (-2*m+2) + (n//2)*(6*m-7)
else:
    c = (m-1) + (n//2) * (6*m-7)
wall = cell * 6 - c
print(wall)

