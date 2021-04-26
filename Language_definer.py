# -*- coding: utf-8 -*-
import os
import codecs
print(os.getcwd())
os.chdir(r'C:\Users\asus\Documents\C2')
print(os.getcwd())
path='C:\\Users\asus\Documents\C2'
files=os.listdir(path='.')
k=1000
filess=[0]*(k+1)
for i in range(k):
    cor=files[i].find('.')
    filess[int(files[i][:cor])]=files[i]
print(filess)
fout=codecs.open("C2ans1","w","utf-8")
import cld2
for i in range(1,k+1):
    fin=codecs.open(filess[i],'r',"utf-8")
    s=fin.read()
    isReliable, textBytesFound, details=cld2.detect(s)
    lang=details[0][1]
    percent1=details[0][2]
    percent2=details[1][2]
    percent3=details[2][2]
    lang2=details[1][1]
    lang3=details[2][1]
    blok=0
    if blok==1:
        print(lang,end=' ')
        print(percent1,end=' ')
        print(lang2,end=' ')
        print(percent2,end=' ')
        print(lang3,end=' ')
        print(percent3,end=' ')
        print('\n')
    print(lang)
    fout.write(lang+"\n")
    fin.close()
fout.close()