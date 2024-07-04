num=int(input("Enter the nummber:"))
if num > 2:
  for i in range(2,num):
      if (num % i)==0:
          print(num,"is prime number")
          break
      else:
         print(num,"is not prime number")
         break
      
      
      
