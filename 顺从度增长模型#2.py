pass    #蠢驴引擎使用定点数，该程序使用整数代替，并将结果转化
def Q(V):    #取整器，改成向下取整
    if V<0:
        return int(V-1)
    else:
        return int(V)   #蠢驴还真的用的向下取整
def L(C):
    global l
    return C/100000*l    #计算高顺从度影响
def T(z):
    return z*0.001    #将该程序使用的整数转为蠢驴的定点数
def R(x):
    return x*1000    #上一个函数的反函数
u=75    #基础顺从度增长是个常量
print("基础顺从度日增长："+str(T(u)))
a=eval(input("请输入顺从度增长额外修正值之和（默认是0，不要输入空值！）："))
b=eval(input("请输入顺从度增长百分比修正之和（单位为%，不要输入空值！）："))
print("请确认输入数值，综合额外修正值："+str(a)+"；综合修正度："+str(b)+"%。")
print("如输入有误，请重启程序！")
input("确认输入无误后按回车键继续")
a=R(a)
b=b*0.01
g=u*(1+b)+a
l=83    #高顺从度影响系数，不受其他修正影响 
print("高顺从度影响上限："+str(T(l)))
d=0
c=0    #必须是整数，不应超过“平衡值”
c=eval(input("请输入初始顺从度（通常是0，不要带“%”）："))
print("初始顺从度："+str(c)+"%")
c=R(c)
s=g-Q(L(c))
s=Q(s)    #取整，第一天的顺从度增长
print("初始顺从度增长："+str(T(s))+"%")
ls=["天数","顺从度","顺从度增长"]    #制表
fl=open("顺从度增长计算结果.csv","w")    #创建csv文件
fl.write(",".join(ls)+"\n")  #将结果写入对应的csv文件，下同
ls=[str(d),str(T(c)),str(T(s))]
fl.write(",".join(ls)+"\n")
print(ls[0]+"天后顺从度："+ls[1]+"(+"+ls[2]+")")   #如果顺从度增长变为负了就会出显示上的小问题
Y=0    #用于中断循环的变量
while Y==0:
    if s<=0:    #判断顺从度是否继续增长
        break    
    c=c+s
    d+=1
    if c>=100000:   #判断顺从度是否超过100.000%
        c=100000
        Y=1
    s=g-Q(L(c))
    s=Q(s)    #取整
    ls=[str(d),str(T(c)),str(T(s))]
    print(ls[0]+"天后顺从度："+ls[1]+"(+"+ls[2]+")")
    fl.write(",".join(ls)+"\n")
print("上述结果已输出到和该程序相同目录下！")
print("顺从度停止增长")
print("顺从度上限："+str(T(c)))
s=g-Q(L(c))
s=Q(s)    #取整
print("最终顺从度日变化："+str(T(s)))
fl.close()
input("程序运行结束，按回车键以关闭程序")
