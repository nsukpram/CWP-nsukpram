import sys
if len(sys.argv) != 3 :
    print("none")
else :
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    if a < b :
        l = list(range(a,b+1))     # ที่ b+1 จะไม่ทำงาน ก็หยุดที่ b พอดี
        print(l)
    else :
        l = list(range(a,b-1,-1))
        print(l)