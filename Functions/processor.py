def process_numbers(lista):
    num = []
    if isinstance(lista, list) == False:
        return num

    for item in lista:
        if isinstance(item, int):
            num.append(item)
        elif isinstance(item, str):
            if item.isnumeric():
                converted = int(item)
                num.append(converted)
    num.sort()
    return num


def process_names(lista):
    names = []
    if isinstance(lista, list) == False:
        return names

    for item in lista:
        if isinstance(item, str):
            if item.isnumeric() == False:
                names.append(item)
    names.sort()
    return names
