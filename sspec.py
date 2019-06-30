gh=input()
dol=0
for i in range(len(gh)):
    if(gh[i].isdigit() or gh[i].alpha() or gh[i].(" ")):
           continue
    else:
       dol+=1
 print(dol)
