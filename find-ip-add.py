import socket
hostname=socket.gethostname()
ipAdd=socket.gethostbyname(hostname)
print("your computer name is:"+hostname)
print("your computer Ip Address is:"+ipAdd)






import socket
inputval=input("Enter the IpAddress:")
hostname=socket.gethostname()
ipAdd=socket.gethostbyname(hostname)
print("your computer name is:"+hostname)
print("your computer Ip Address is:"+ipAdd)
if inputval==ipAdd:
    print("it matches with the entered value.")
else:
        print("it does not match!")
