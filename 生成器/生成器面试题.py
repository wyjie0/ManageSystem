def demo():
     for i in range(4):
         yield i

g = demo()

g1 = (i for i in g)
g2 = (i for i in g1)

print(list(g1))
print(list(g2))