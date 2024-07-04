tempvar=int(input("Enter a channel number:"))
print(tempvar)
if tempvar%5==0:
  print("channel number" + str(tempvar) + "belongs to vijay")
elif tempvar%7==0:
  print("channel number" + str(tempvar) + "belongs to zee")
else:
  print("channel number" + str(tempvar) + "belongs to other")
