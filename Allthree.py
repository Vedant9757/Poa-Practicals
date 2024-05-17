def printTable(blockSizes, processSizes):         
     print("\nProcess ID\t\t\tProcess Size\t\t\tBlock Size")
     for i, (key, value) in enumerate(processSizes.items()):
        print(f'P{i+1}\t\t\t\t{key}\t\t\t\t{value}')

def printQuestion(blockSizes, processSizes):
    print("Block Sizes", end=": ")
    for key in blockSizes.keys():
        print(key, end=" ")
    print("\nProcess Sizes: ", end="")
    for key in processSizes.keys():
        print(key, end=" ")

def fragmentation(blockSizes, processSizes):
    internalFrag = 0
    externalFrag = 0
    for key in processSizes.keys():
        if(processSizes.get(key) == -1):
            continue
        internalFrag +=  processSizes.get(key) - key
    for key in blockSizes.keys():
        if(blockSizes.get(key) == -1):
            externalFrag += key
    print(f"Internal Fragmentation: {internalFrag}")
    print(f"External Fragmentation: {externalFrag}")


    
def firstFit(blockSizes,processSizes):
    print("FIRST FIT\n")
    blockSizes = {key: -1 for key in blockSizes}
    processSizes = {key: -1 for key in processSizes}
    printQuestion(blockSizes, processSizes)
    

    for pSize in processSizes.keys():
        for bSize in blockSizes.keys():
            if(bSize>=pSize and blockSizes.get(bSize) ==-1):
                blockSizes.update({bSize:pSize})
                processSizes.update({pSize: bSize})
                break

    printTable(blockSizes, processSizes)
    fragmentation(blockSizes, processSizes)


def worstFit(blockSizes,processSizes):
    blockSizes = {key: -1 for key in blockSizes}
    processSizes = {key: -1 for key in processSizes}
    printQuestion(blockSizes, processSizes)
    for pSize in processSizes.keys():
        max = -1
        for bSize in blockSizes.keys():
            if(bSize>=pSize):
                if(max<bSize and blockSizes.get(bSize)==-1):
                    max=bSize
        
        blockSizes.update({max:pSize})
        processSizes.update({pSize: max})
    print("\nWORST FIT")

    printTable(blockSizes, processSizes)
    fragmentation(blockSizes, processSizes)




def bestFit(blockSizes, processSizes):
    print("BEST FIT\n")
    blockSizes = {key: -1 for key in blockSizes}
    processSizes = {key: -1 for key in processSizes}
    printQuestion(blockSizes, processSizes)
    
    for pSize in processSizes.keys():
        allocatedB = -1
        allocatedP = -1
        for bSize in blockSizes.keys():
            if bSize >= pSize and blockSizes.get(bSize)==-1:
                if(allocatedB ==-1 or allocatedB>bSize):
                    allocatedP = pSize
                    allocatedB = bSize

        if allocatedB != -1:
            blockSizes[allocatedB] = allocatedP
            processSizes[allocatedP] = allocatedB


    printTable(blockSizes, processSizes)
    fragmentation(blockSizes, processSizes)




blockSizes = {100:-1, 500:-1, 200:-1, 300:-1, 600:-1}
processSizes ={212 : -1, 417:-1, 112:-1, 426:-1} 

firstFit(blockSizes, processSizes)
print("\n\n")

bestFit(blockSizes, processSizes)
print("\n\n")

worstFit(blockSizes, processSizes)
print("\n\n")