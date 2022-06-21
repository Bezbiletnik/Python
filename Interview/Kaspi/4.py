a = input().lower()
print(*[f"{x}:{a.count(x)}" for x in set(a) if x.isalpha()])
