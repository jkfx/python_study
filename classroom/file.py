def isnumber(str1):
    count = 0
    for i in str1:
        if i >= '0' and i<='9':
            count += 1
    return count
t1 = open('fx.txt')
list1 = t1.readlines()
list2 = list(map(isnumber, list1))
print(list2)
