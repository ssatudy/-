def func(lst):
    lst_ordered = sorted(lst)
    result = 0
    for idx, i in enumerate(lst_ordered):
        if idx % 2 != 0:
            result += i

    return result

    