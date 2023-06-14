def abbreviation():
    input_string = input("Enter a string")
    print(input_string)
    input_string = input_string.split(" ")
    print(input_string)
    print(type(input_string))
    res = []
    print(res)
    for ele in input_string:
        if len(ele) == 2:
            res.append(ele[0].lower())
        if len(ele) > 2:
            res.append(ele[0].upper())
        if len(ele) < 2:
            continue

    print(res)
    print("".join(res))


abbreviation()
