frameno=int(input("Enter No. of frames :- "))
pageno=int(input("Enter No. of pages :- "))
frames=[-1]*frameno
pages=[]
hit=0
miss=0
for i in range(pageno):
    pages.append(int(input("Enter Pages :- ")))
    print("Pages:- ",pages)
def find_lru(i):
    point=[-1]*frames
    for j in range(frameno):
        for k in range(i):
            if(frames[j]==pages[k]):
                point[j]=k
    lru=pages[min(point)]
    return lru
        
    

