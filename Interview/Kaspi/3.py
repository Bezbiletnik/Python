n = int(input())
a = int(input())
b = int(input())

print(a)
print(b)
for _ in range(2, n):
    a, b = b, a+b
    print(b)

