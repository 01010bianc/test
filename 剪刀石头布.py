#1代表剪刀，2代表石头，3代表布
#剪刀大于布，布大于石头，石头大于剪刀
#即1>3,3>2,2>1
import random
a = random.randint(1,3)
player = int(input())

if player == a:
    print(a)
    print('平局，再比一次')
elif player == 1:
    if a==2:
        print(a)
        print('你输了！！！')
    else:
        print(a)
        print('你赢了！')
elif player == 2:
    if a==1:
        print(a)
        print('你赢了！')
    else:
        print(a)
        print('你输了！！！')
else:
    if a == 1:
        print(a)
        print('你输了！！！')
    else:
        print(a)
        print('你赢了！！！')

