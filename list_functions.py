def flattenList(toFlatten):
    flattened = []

    for element in toFlatten:
        if type(element) is list:
            for item in element:
                flattened.append(item)
        else:
            flattened.append(element)

    return flattened

if __name__ == '__main__':
    print(flattenList([[1,2],[3],[4,5,6]]))
