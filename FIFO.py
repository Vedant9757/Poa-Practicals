frameno=int(input("Enter No. of frames :- "))
pageno=int(input("Enter NO. of pages :- "))
pages =[]
frames =[-1]*frameno
hit =0
miss =0
for i in range (pageno):
    pages.append(int(input("Enter pages :- ")))
    print("Pages :- ",pages)
k=0
for i in range (len(pages)):
    if pages[i] in frames:
        hit += 1
        print("Page ",pages[i]," Hit")
    else:
        miss += 1
        frames[k]=pages[i]
        print("Page ",pages[i]," loaded in frame ",k)
        k=(k+1)%frameno

print("Last frame :- ",frames)
print("Total page miss :- ",miss)
print("Total page hit :- ",hit)
re2=miss/(miss+hit)
print("Miss ratio :- ",re2*100)
re1=hit/(miss+hit)
print("Hit ratio :- ",re1*100)    
        