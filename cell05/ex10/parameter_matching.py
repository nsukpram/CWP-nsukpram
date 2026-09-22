import sys
if len(sys.argv) != 2 :
    print("none")
else :
    text = input("What was the parameter? ").strip()
    if text == sys.argv[1] :
        print("Good job!")
    else :
        print("Nope, sorry...")