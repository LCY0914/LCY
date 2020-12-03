list1 = [i for i in range(1,51)]
print(list1)
k = 0
while len(list1)>3 :
    i = 0
    while i<len(list1):
        k += 1
        if k == 4:      # 遇4杀人 
            list1.remove(list1[i])
            k =0 
        else:
            i +=1
print(list1)