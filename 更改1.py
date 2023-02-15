
x=float(input('输入一个数：'))   
y=float(int(x))     #如果x为小数进行取整

Rs=[]               #创建列表
if x==0:
    Rs.append('0')  #输出当x=0的结果
else:
                    #计算如果x>0的结果
    if x>0:
        n=0
        if y==0:
            Rs.append('0')
        else:
            while y>=2**n:
                n+=1     #得出x>=2**n中n的最大值，便于进行位数确定

                                  #计算x整数部分的二进制数
            for i in range(0,n):
                if y>=2**(n-1):
                    y=y-2**(n-1)
                    Rs.append('1')   #当x-2**n（n从最大值依次输入）成立时，将1输入列表
                    n=n-1
                else:
                    n=n-1
                    Rs.append('0')  #当x-2**n（n从最大值依次输入）不成立时，将0输入列表

                                   #计算x的小数部分
        y=float(int(x))            #重新输入y的值
        z=float(x-y)
        Rs.append('.')
        if z==0:
            Rs.append('0')
        else:
            m=0
            for o in range(0,8):
                if z>=2**(m-1):
                    z=z-2**(m-1)
                    Rs.append('1')
                    m=m-1
                elif z==0:
                    continue
                else:
                    m=m-1
                    Rs.append('0')
    else:                          #计算如果x为负数时
        x=-x
        y=-y
        Rs.append('-')
        n=0
        if y==0:
            Rs.append('0')
        else:
            while y>=2**n:
                n+=1


            for i in range(0,n):
                if y>=2**(n-1):
                    y=y-2**(n-1)
                    Rs.append('1')
                    n=n-1
                else:
                    n=n-1
                    Rs.append('0')


        y=float(int(x))            
        z=float(x-y)
        Rs.append('.')
        if z==0:
            Rs.append('0')
        else:
            m=0
            for o in range(0,8):
                if z>=2**(m-1):
                    z=z-2**(m-1)
                    Rs.append('1')
                    m=m-1
                elif z==0:
                    continue
                else:
                    m=m-1
                    Rs.append('0')
        
for each in range(0,len(Rs)):
    print(Rs[each],end='')
