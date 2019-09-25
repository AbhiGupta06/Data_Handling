
list1 = [13,1,13,1,13,2,1,13]
list2 = []
for i in range(0,len(list1)):
    if list1[i]==13 and i<len(list1)-1 and list1[i]!=list1[i+1] and list1[i]!=list1[i+2] :
        list2.append(list1[i+2])
        
print(sum(list2))