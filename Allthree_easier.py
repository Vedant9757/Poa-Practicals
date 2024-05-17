def best_fit(mem, pr):
    mem.sort()
    print("Best Fit Allocation:")
    for i in range(len(pr)):
        for j in range(len(mem)):
            if pr[i] <= mem[j]:
                print(f"Allocate {pr[i]} at {mem[j]}")
                mem[j] = 0
                break

def worst_fit(mem, pr):
    mem.sort(reverse=True)
    print("Worst Fit Allocation:")
    for i in range(len(pr)):
        for j in range(len(mem)):
            if pr[i] <= mem[j]:
                print(f"Allocate {pr[i]} at {mem[j]}")
                mem[j] = 0
                break

def first_fit(mem, pr):
    print("First Fit Allocation:")
    for i in range(len(pr)):
        for j in range(len(mem)):
            if pr[i] <= mem[j]:
                print(f"Allocate {pr[i]} at {mem[j]}")
                mem[j] = 0
                break

def main():
    memno = int(input("Enter Memory Number: "))
    prono = int(input("Enter Process Number: "))
    
    mem = []
    pr = []
    
    for i in range(memno):
        mem.append(int(input("Enter Memory Size: ")))
    
    for i in range(prono):
        pr.append(int(input("Enter Process Size: ")))
    
    print("Process Sizes:", pr)
    print("Memory Sizes:", mem)
    
    # Make copies of the memory list to use for each fit method
    mem_best_fit = mem[:]
    mem_worst_fit = mem[:]
    mem_first_fit = mem[:]
    
    best_fit(mem_best_fit, pr)
    print()  # For better readability
    worst_fit(mem_worst_fit, pr)
    print()  # For better readability
    first_fit(mem_first_fit, pr)

if __name__ == "__main__":
    main()