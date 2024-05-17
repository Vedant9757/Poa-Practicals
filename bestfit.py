memno=int(input("Enter Memory No. :- "))
prono=int(input("Enter Process No. :- "))
mem=[]
pr=[]

for i in range (memno):
    mem.append(int(input("Enter Memory Size :- ")))
for i in range (prono):
    pr.append(int(input("Enter Process Size :- ")))

mem.sort()
print(pr)
print(mem)

for i in range(len(pr)):
    for j in range(len(mem)):
        if(pr[i]<=mem[j]):
            print("Allocation ",pr[i],"at ",mem[j])
            mem[j]=0
            break        
    