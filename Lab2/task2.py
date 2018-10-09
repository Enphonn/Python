with open('file.txt',encoding='cp1251') as file:
    array2d = [[digit for digit in line.split()] for line in file]

for i in array2d:
    for j in i:
        m =j.replace(',','')
        #j.replace('.','')
        j =m

dic={}
for i in array2d:
    for j in i:
        if(j[-3:] not in dic):
           dic[j[-3:]] = []

        dic[j[-3:]].append(j)


print(dic)