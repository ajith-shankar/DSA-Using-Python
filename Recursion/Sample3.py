res=[]
for ele in inputstring:
    if len(ele) == 2:
        res.append(ele[0].lower())
    if len(ele) > 2:
        res.append(ele[0].upper())
    if len(ele) < 2:
        continue

    return "".join(res)