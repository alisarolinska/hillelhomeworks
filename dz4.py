def to_dict(list):
    for element in list:
        return{element: element}


lst = [1, 2, 3, 4, 5, 6, 7, 8]

print(to_dict(lst))
