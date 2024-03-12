
def stateQ0(n, countzero, countone):
    print("Q0->", end="")
    if (len(n) == 0):
        print("\nTotal no of 1 :", len(countone))
        print("Total no of 0 :", len(countzero))
    else:
        if(n[0]=="0"):
            countzero.append("0")
            stateQ0(n[1:], countzero, countone)
        elif (n[0] == "1"):
            countone.append("1")
            stateQ0(n[1:], countzero, countone)


countzero = []
countone = []
n = input("Enter number of 0 & 1: ")
print("Transition State: ")
stateQ0(n,countzero,countone)
