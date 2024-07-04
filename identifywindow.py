import platform
import os
osidentifier=platform.platform()
print(osidentifier)
if "Windows" in osidentifier:
    print("underlying os is window")
    cmdstring="ipconfig"
elif "drawn" in osidentifier or "sonam" in osidentifier:
    print("underlying os is mac")
    cmdstring="ifconfig"
else:
    print("underlying os is linx")
    cmdstring="ifconfig"
var=os.popen(cmdstring).read()
print(var)

