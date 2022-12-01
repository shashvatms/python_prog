lst1 = []
i = int(input("number of numbers: "))
for x in range(1,i+1):
    x = int(input("enter number: "))
    lst1.append(x)
    x+=1
for y in range(0,len(lst1)):
    x = lst1[y]
    a = 0
    b = 1 
    lst = [0,1]
    while a < 10000:
        lst.append(a)
        a,b = b,a+b
    if x in lst:
        print(x,"is vallid")
    else:
        print(x,"is invallid")
