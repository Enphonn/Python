def function(x, y):
    if x < 0 or y < 0:
        raise Exception('The number is negative.')
    res = False
    if x%y == 0:
        res = True
    return res

print(function(x = int(input('Enter x: ')),y = int(input('Enter y: '))))