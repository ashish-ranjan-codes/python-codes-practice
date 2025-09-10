# find largest of three numbers

a,b,c = map(int, input("Enter three numbers separated by space: ").split())

if a > b:
    if a > c:
        print(f"{a} is largest.")
    else:
        print(f"{c} is largest.")
elif b > c:
    print(f"{b} is largest.")
else:
    print(f"{c} is largest.")
