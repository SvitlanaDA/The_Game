x = int(500)
y = int(500)
print(x is y)
p = int(10)
q = int(10)
print (p is q)
print (id (p))
print (id (q))
print (id(p) == id(q))
p += 0
print (id (p))
print (id (q))
print (id(p) == id(q))
print (p is q)