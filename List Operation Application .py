#List Opreation Python Application
while True:
  print("--------------------------------------")
  print("               App-Menu               ")
  print("--------------------------------------")
  print("press 0 to create new list")
  print("press 1 for add element")
  print("press 2 for replace value")
  print("press 3 for remove value")
  print("press 4 read value")
  print("press 5 for Exit")
  print("--------------------------------------")
  op=int(input("Select Any Option:"))
  new=''
  if op==0:
    new=list(new)
    print(new,"Created.............")
  elif  op==1:
    a=int(input("Enter element to add into the list:"))
    new.append(a)
    print(list)
  elif op==2:
    x=int(input("Enter index no to replace: "))
    y=int(input("Enter new value to replace: "))
    new[x]=y
    print("Value replace successfully:",new)
  elif op==3:
    x=int(input("Enter Number to remove: "))
    new.remove(x)
    print("Value remove successfully:",new)
  elif op==4:  
    print(new)
  elif op==5:
    print("Thanks for using My App") 
    break
  else:
    print("Select correct option")


      