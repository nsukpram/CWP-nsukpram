import sys
import re
if len(sys.argv) != 3 :
    print("none")
else :
    matches = re.findall(sys.argv[1],sys.argv[2])
    if not matches :
        print("none")
    else :
        print(len(matches))