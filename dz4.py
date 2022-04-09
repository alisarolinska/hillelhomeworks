def to_dict(list):
    return {element: element for element in list}


lst = [1, 2, 3, 4, 5, 6, 7, 8]

print(to_dict(lst))
