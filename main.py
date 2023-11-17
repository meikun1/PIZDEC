def change(lst):
    start = lst.pop()
    end = lst.pop(0)
    lst.append(end)
    lst.insert(0, start)
    return lst
print(change([1, 2, 3, 5, 8, 9]))
