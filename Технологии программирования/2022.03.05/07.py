lt = ['myfile1.txt','myfile2.png' , 'Myfile3.py', 'my_file.TXT', 'my_fiLE.TXT', 'MY_file.Txt', 'myfILE1.Txt']
search_in = input("Расширение str > ")
ltype = {(s.split('.')[0].lower(), s.split('.')[1].lower()) for s in lt if s.split('.')[1].lower() == search_in.lower()}
print(*sorted(ltype), sep=' ')