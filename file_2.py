#use of file using block


with open("fi_1.txt",'r') as f:#dont need to close the file
    data=f.read()
    print(data)
print(f.closed)
#for writiing u can use w ,a,r+
#for w mode ------>
# with open("fi_2.txt",'w') as f:
#     f.write("hello")
with open("fi_3.txt",'a') as f:
    n=int(input("enter line nos:"))
    for i in range(0,n):
           f.write(input("enter text:"))