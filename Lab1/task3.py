def function(arr):
    res = []
    for i in arr:
        if (type(i) == list or type(i) == tuple):
            function(i)
        else:
            res.append(i)
    return res

print(function(arr = ['a', ['c', 1, 3], ['f', 7, [4, '4']], [{'lalala': 111}]]))