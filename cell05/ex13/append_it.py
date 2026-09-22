import sys
import re
l = sys.argv[1:]
if not l :
    print("none")
else :
    for i in l :
        if not re.match(".*ism",i) :
            print(f"{i}ism")