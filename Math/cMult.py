def cMult(u, v):
    return [u[0]*v[0] - u[1]*v[1], u[0]*v[1] + u[1]*v[0]]

u = [1, 2]
v = [3, 4]

print(cMult(u, v))
