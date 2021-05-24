ab=[1,2,3,4]
et=filter(lambda a: a%2==0,ab)
vc=map(lambda a:a**2,ab)
print(next(et))
print(list(et))
print(next(vc))