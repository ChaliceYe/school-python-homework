n=0
level1=input("请输入第一个等级：")
if level1=="A":
    n=n+1
else:
    n=n+2
level2=input("请输入第二个等级：")
if level2=="B":
    n=n+2
else:
    n=n+1
print("总分为:",n)
