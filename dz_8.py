result = []
def checker(key):
    if type(key)  != str:
        raise TypeError(f"Sorry,we can't work with{key},we need class str")
    else:
        return key



def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a/b
data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8 : 4}
for key in data:
    res = divider(key, data[kem])
    result.append(res)

print(result)
