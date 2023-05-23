def mysplit(strng):
    strng = strng.strip()
    lst = []
    if strng == "":
        return lst
    else:
        word = ""
        for i in range(len(strng)):
            if strng[i] == " ":
                if word != "":
                    lst.append(word)
                    word = ""
            else:
                word += strng[i]
        if word != "":
            lst.append(word)
        return lst


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
