with open("test.html",'r') as webpage:
    with  open("output.txt",'a') as wf:
        for line in webpage.readlines():
            if '<a href=' in line:
                pos=line.find('<a href=')
                first_q=line.find('\"',pos)
                second_q=line.find('\"',first_q+1)
                url=line[first_q+1:second_q]
                wf.write(url+'\n')