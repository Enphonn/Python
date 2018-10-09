import random
def task1(file):

    lines =open(file,encoding='cp1251').read().splitlines()
    myline =random.choice(lines)
    print(myline)

def task2():
    b1=open("b1.txt",'w')
    b2=open("b2.txt",'w')
    f = open('file.txt').read().splitlines()
    for i in range(len(f)):
        if(i%2==0):
            b2.write(f[i].lower()+'\n')
        else:
            b1.write(f[i].upper()+'\n')
    b1.close()
    b2.close()


task1('file.txt')
task2()