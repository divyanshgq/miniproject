print("-----Welcome to Voting booth-----")
unique=[]
countb=0
countc=0
counta=0
countt=0
while True:
    n0=input("Enter your full name: ")
    n1=int(input("Enter your age: "))
    if n1>=18:
        n2=int(input("Enter your unique code: "))
    else:
        print("We appreciate your enthusiasm but you will be eligible to vote in",18-n1,"years")
        cont=input("Do you wish to continue type y/n: ")
        if cont=="Y" or cont=="y":
            continue
        else:
            break
    if n2 in unique:
        print("----You have already voted once-----")
        break
    else:
        unique.append(n2)
    party=int(input("""-----Choose the Party you wish to vote for (Type serial no. to choose)-----
    1. BJP
    2. Congress
    3. AAP
    4. TMC
    """))
    if party==1:
        countb+=1
    elif party==2:
        countc+=1
    elif party==3:
        counta+=1
    elif party==4:
        countt+=1
    else:
        print("Choose a valid Party(Type serial no. to choose)")
    cont2=input("Do you wish to continue type y/n: ")
    if cont2=="Y" or cont2=="y":
        continue
    else:
        break
print("Number of votes for bjp: ",countb)
print("Number of votes for congress: ",countc)
print("Number of votes for aap: ",counta)
print("Number of votes for tmc: ",countt)