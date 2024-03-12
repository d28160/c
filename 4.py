
#prac 4

def stateQ0(inputstr):
    print("Q0->", end="")
    if(len(inputstr)<=2):
        print("\nString Rejected")
    elif(inputstr[0] == "0"):
        stateQ0(inputstr[1:])
    elif(inputstr[0] == "1"):
        stateQ1(inputstr[1:])

def stateQ1(inputstr):
    print("Q1->", end="")
    if(len(inputstr)<=1):
        print("\nString Rejected")
    elif(inputstr[0] == "0"):
        stateQ0(inputstr[1:])
    elif(inputstr[0] == "1"):
        stateQ2(inputstr[1:])

def stateQ2(inputstr):
    print("Q2->", end="")
    if(len(inputstr)<=0):
        print("\nString Rejected")
    elif(inputstr[0] == "1"):
        stateQ3(inputstr[1:])
    elif(inputstr[0] == "0"):
        if len(inputstr)<2:
            print("\nString Rejected")
        else:
            stateQ0(inputstr[1:])

def stateQ3(inputstr):
    print("Q3->", end="")
    if(len(inputstr)<=0):
        print("\nString Accepted")
    elif(inputstr[0] == "0"):
        stateQ3(inputstr[1:])
        print("Q3->", end="")
    elif(inputstr[0] == "1"):
        stateQ3(inputstr[1:])
        print("Q3->", end="")

inputstr = input("Enter string of 0 and 1: ")
lenstr = len(inputstr)
print(lenstr)
if lenstr < 3:
    print("Enter a string of atleast 3 char.")
elif lenstr == "111":
    print("Q0->Q1->Q2->Q3")
    print("\nString Accepted")
else:
    stateQ0(inputstr)
