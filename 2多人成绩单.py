stulist=[]
student={}
student={"姓名":"王静","学号":"00221325","语文":125,"数学":135.5,"英语":140}
stulist.append(student)
student={"姓名":"张子栋","学号":"00221331","语文":123,"数学":132.5,"英语":111}
stulist.append(student)
student={"姓名":"王小明","学号":"00221316","语文":112,"数学":125,"英语":130}
stulist.append(student)
stulist[0]["总分"]=stulist[0]["语文"]+stulist[0]["数学"]+stulist[0]["英语"]
stulist[1]["总分"]=stulist[1]["语文"]+stulist[1]["数学"]+stulist[1]["英语"]
stulist[2]["总分"]=stulist[2]["语文"]+stulist[2]["数学"]+stulist[2]["英语"]
print("现在已经有",str(len(stulist)),"位同学成绩，他们的得分如下")
for score in range(len(stulist)):
    print("学号",stulist[score]["学号"],"姓名",stulist[score]["姓名"],"语文",stulist[score]["语文"],"数学",stulist[score]["数学"],"英语",stulist[score]["英语"],"总分",stulist[score]["总分"])
