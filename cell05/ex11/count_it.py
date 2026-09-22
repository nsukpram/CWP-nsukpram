import sys
p = sys.argv[1:]
if not p:
    print("none")
else :
    print(f"parameters: {len(p)}")
    for i in p :
        print(f"{i}: {len(i)}")