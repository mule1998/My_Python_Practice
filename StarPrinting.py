n=int(input("Enter number of star rows"))
boolean=int(input("Enter number which is greater than or less than 5 Do not enter 5"))

if boolean>5:
  print("true")
  for i in range(0,n):
    for j in range(0,i+1):
      print("*",end=" ")
    print()

else:
  print("false")
  for i in range(0,n):
    for j in range(n-i):
      print("*",end=" ")
    print()
    
