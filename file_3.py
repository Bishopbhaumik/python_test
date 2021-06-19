#using r+ we can read and write it and r+ mode can not create file
with open("fi_3.txt",'r+') as f:
    f.seek(len(f.read()))
    f.write("\t please do it")