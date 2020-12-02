import random
n=int(random.random()*50+1)
i=1
while i<=5:
    cin= int(input("请输入你要猜的数字："))
    if(cin<n):
        print("你输入的数字较小")
        i = i+1
    elif(cin>n):
        print("你输入的数字较大")
        i = i+1
    elif n == cin:
        print("恭喜你猜对啦")
        break
else:
    print("你已经猜了五次，你输啦")
```