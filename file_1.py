#read file
#open function
#read method
#seek method
#tell method
#readline method
#readlines method
#close method
f=open("fi_1.txt")#naturally opens in reading can define by writing and reading modes
print(f"cursor position--->{f.tell()}")
print(f.read())
print(f"cursor position--->{f.tell()}")
f.seek(0)
print(f"cursor position--->{f.tell()}")
print(f.read())
f.seek(0)
print(f.readline(),end='')
print(f.readline(),end='')
# print(f.readline(),end='')
print(f.closed)
f.close()
print(f.closed)