def function(x, y):
    if (x > y):
        x, y = y, x
    array = []
    for i in range(x, y+1):
        if i > 0:
            for j in range(2, i):
                if (i % j) == 0:
                    break
            else:
                    array.append(i)
    if array != []:
        print(array)
    else:
        raise Exception('NoSimpleDigits')

print(function(x = int(input('Enter x: ')),y = int(input('Enter y: '))))
