def last(n):
    return n[-1]

def sort(tuple):
    return sorted(tuple, key=last)

a =[(2,5),(1,2),(2,3),(4,4),(2,3),(2,1)]
print("expected output:")
print(sort(a))     