#高级计算机
#by:邝宇轩

#函数区
        
def mj():#面积
    try:
        a=int(input ('请输入长度'))#长度
        s=int(input ('请输入宽度'))#宽度
        print('面积')
        print(a*s)
        print('\n')
    except:
        print('请输入数字')
        print('\n')


def dp():#地皮
    try:
        a=int(input('请输入长度'))#长度
        s=int(input('请输入宽度'))#宽度
        d=int(input('物品的价格是多少？'))#物品的价钱
        print('物品总共')
        print(a*s*d)
        print('元')
        print('\n')
    except:
        print('请输入数字')
        print('\n')


def a404():
    print('计算方式错误')
    print('\n')


def cg():#常规计算

    
    if fs==1:#加
        print(shu_1+shu_2)
        print('\n')
        
    elif fs==2:#减
        print(shu_1-shu_2)
        print('\n')
        
    elif fs==3:#乘
        print(shu_1*shu_2)
        print('\n')
        
    elif fs==4:#除
        print(shu_1/shu_2)
        print('\n')
        
    elif fs==5:#求余
        print(shu_1/shu_2%2)
        print('\n')

    else:#报错
        a404()


def ts():#特殊计算模式
    try:
        tsfs=int(input('请选择方式(1=计算面积,2=计算地毯等物品价格,3=计算BIM)'))
    except:
        print('请输入数字')
        print('\n')
    if tsfs==1:#计算面积
        mj()

    elif tsfs==2:#计算地毯、地板、草皮等价格
        dp()

    elif tsfs==3:#计算BIM
        BIM()
        
    else:#报错
        a404()

def BIM():#计算BIM
    try:
        w=float(input('请输入体重（千克）：'))
        h=float(input('请输入身高（米）：'))
        
        print('你的BMI：',w/h**2)
        print('\n')
        
    except:
        print('请输入数字')
        print('\n')



#主程序模块
while True:
    
    #询问模块
    try:
        fs=int(input('选择计算方式(0=停止,1=加,2=减,3=乘,4=除,5=求余,6=小学题计算模式)'))
        if fs==0:#停止
            print('正在退出')
            print('\n')
            break

    #特殊计算模块
        elif fs==6:#小学题计算模式
            ts()
            continue
    except:
        print('请输入数字')
        print('\n')
        continue
   

    #常规计算模块
    try:
        shu_1=int(input('请输入第一个数'))
        shu_2=int(input('请输入第二个数'))
        cg()
    except:
        print('请输入数字')
        print('\n')
        
    continue
