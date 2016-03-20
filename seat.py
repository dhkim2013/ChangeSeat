import random

def do():
    global blist,bad,seat,randList
    randList=[]
    cnt=0
    for i in range(bad):
        tmp=random.randint(1,15)
        while 1:
            check=0
            for j in range(cnt):
                if tmp==randList[j]:
                    tmp=random.randint(1,15)
                    check=1

            if check==0:
                randList.append(tmp)
                cnt+=1
                break

    for i in range(bad):
        seat[randList[i]]=blist[i]

def do2():
    global seat,randList,list,randList2,person,bad,c
    randList2=[]
    cnt=0
    for i in range(person-bad):
        tmp=random.randint(1,person)
        while 1:
            check=0
            if c==1:
                for j in range(len(randList)):
                    if tmp==randList[j]:
                        tmp=random.randint(1,person)
                        check=1

            for j in range(cnt):
                if tmp==randList2[j]:
                    tmp=random.randint(1,person)
                    check=1

            if check==0:
                randList2.append(tmp)
                cnt+=1
                break

    for i in range(person-bad):
        seat[randList2[i]]=list[i]


person=input('How many student? ')
c=0
seat={}
list=[]
for i in range(person):
    list.append(i+1)

bad=input('How many bad eyesight student? ')
blist=[]
if bad>0:
    print 'Input student number'
    for i in range(bad):
        tmp=input('[%d] : '%(i+1))
        blist.append(tmp)
        list.remove(tmp)

row=input('How many rows? ')
if bad>0:
    c=1
    do()
do2()
user=raw_input('Do you want save file?(Y/N) ')
if user=='Y' or user=='y':
    f=open("seat.txt",'w')
for i in range(person):
    if i>0 and i%row==0:
        print ''
        if user=='Y' or user=='y':
            f.write('\n')
    data='%d\t'%(seat[i+1])
    print data,
    if user=='Y' or user=='y':
        f.write(data)

    if user=='Y' or user=='y':
        f.close()
