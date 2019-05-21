def isnumber(str1):
    count = 0
    for i in str1:
        if i >= '0' and i<='9':
            count += 1
    return count
list1 = ['geek666', '888fx']
list2 = list(map(isnumber, list1))
print(list2)
