#prac 7

def stateq0(n, countzero, countone):
    print("Q0->", end="")
    if(len(n)==0):
        if(len(countzero)==len(countone)):
            print("string accepted")
            print("String having equal no of 1's and 0's")
        else:
            print("String Rejected")
    else:
        if(n[0] == '0'):
            countzero.append('0')
            stateq0(n[1:], countzero, countone)
        elif (n[0] == '1'):
            countone.append('1')
            stateq1(n[1:], countzero, countone)

def stateq1(n, countzero,countone):
    print("Q1->", end="")
    if(len(n)==0):
        if(len(countzero)==len(countone)):
            print("string accepted")
            print("String having equal no of 1's and 0's")
        else:
            print("String Rejected")
    else:
        if(n[0] == '0'):
            countzero.append('0')
            stateq0(n[1:], countzero, countone)
        elif(n[0] == '1'):
            countone.append('1')
            stateq1(n[1:], countzero, countone)

countzero=[]
countone=[]
n=input("Enter 0 and 1 sequence: ")

print("Trannsition state: ")
stateq0(n, countzero, countone)