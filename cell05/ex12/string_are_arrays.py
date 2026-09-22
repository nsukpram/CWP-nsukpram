import sys
l = sys.argv[1:]
if len(l) != 1 :
    print("none")
else :
    c = l[0].count("z")
    if c == 0 :
        print("none")
    else :
        print("z"*c)