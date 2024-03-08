def decryptPassword(s):
    intstring = ""
    result = ""
    icount = 0
    for i in s:
        if i.isdecimal():
            intstring = i+intstring
            icount += 1
        else:
            break
    s = s[icount:]
    count =0
    i =0
    while len(s)-1> i:
        current = s[i]
        nex = s[i+1]
        if current == "*":
            i+=1
            continue
        if current == "0":
            result += intstring[count]
            count += 1
            i+=1
        if current.islower() and nex.isupper():
            result += current
            i+=1
        if current.isupper() and nex.islower():
            result += nex
            result += current
            i+=3
        if current.islower() and nex.isalnum():
            result += current
            i+=1

    if s[-1]==0:
        s[-1]=intstring[count]
    return result+s[-1]
print(decryptPassword("1Bl*Kg*u0"))