import sys

def shrink(s) :
    print(s[:8])
def enlarge(s) :
    print(s+"Z"*(8-len(s)))

l = sys.argv[1:]
if not l:
    print("none")
else :
    for i in l :
        if len(i) == 8 :
            print(i)
        elif len(i) > 8 :
            shrink(i)
        else :
            enlarge(i)