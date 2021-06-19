#better solution
with open('test.html','r') as web:
    with open('output.txt','a') as wf:
        page=web.read()
        link_ex=True
        while link_ex:
                pos=page.find('<a href=')
                if pos==-1:
                    link_ex=False
                else:
                     first_q=page.find('\"',pos)
                     second_q=page.find('\"',first_q+1)
                     url=page[first_q+1:second_q]
                     wf.write(url+'\n')
                     page=page[second_q:]
                    #  page=web.seek(second_q)---->not coming