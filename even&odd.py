inputvar1=int(input("Enter the start range number:"))
inputvar2=int(input("Enter the stop range number:"))
for var in range(inputvar1,inputvar2):
    if var%2==0:
        print("number:"+str(var)+"is even")
    else:
        print("number:"+str(var)+"is odd")







