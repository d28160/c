
#prac 6

def stateQ0(n):
    print("Q0->",end="")
    if len(n) == 0:
        print("String Accepted")
    else:
        if (n[0] == "0"):
            print("Q0->", end="")
            stateQ0(n[1:])
        elif (n[0] == "1"):
            print("Q0->",end="")
            stateQ1(n[1:])

def stateQ1(n):
    print("Q0->",end="")
    if len(n) == 0:
        print("String Not Accepted")
    else:
        if (n[0] == "0"):
            print("Q0->", end="")
            stateQ0(n[1:])
        elif (n[0] == "1"):
            print("Q0->",end="")
            stateQ1(n[1:])

n = int(input("Enter a decimal Number: "))
n = bin(n).replace("0b","")
print(n)
print("Transition State: ")
stateQ0(n)
