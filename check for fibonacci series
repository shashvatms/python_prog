def fib():
    lis = []
    noOfInput = int(input("How many number you  want to enter?"))
    for i in range(0, noOfInput):
        element = int(input("Enter Number: "))
        lis.append(element)
        
    maxNo = max(lis)
    n1, n2 = 0, 1
    list1 = [0]
    if maxNo <= 0:
      print("0 is valid or Negative")
    elif maxNo == 1:
        list1.append(n1)
    else:
      while n2 < maxNo:
          nth = n1 + n2
          n1 = n2
          n2 = nth
          list1.append(nth)
    
    # check no is present or not
    for x in lis:
        if x in list1:
            print(x, "comes in fibonacci series")
        else:
            print(x,"doesn't comes in fibonacci series")
fib()
