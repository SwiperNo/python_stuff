def doube(x,y):
    return x * 2

squence = [1, 3, 5, 9]
doubled = [(lambda x: x * 2)(x) for x in sequence]
doubled = list(map(lambda x: x * 2, squence)}
#map says to iterate of each element in an array and apply the function


