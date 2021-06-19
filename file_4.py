with open("fi_2.txt",'r') as rf:
    with open("fi_3.txt",'w') as wf:
        wf.write(rf.read())