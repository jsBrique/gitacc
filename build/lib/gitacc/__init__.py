import os
import sys


    
def acc():

    print('正在使用git加速器clone')
    target_path = os.getcwd()
    
    if len(sys.argv)==3 and cmd=='clone':
        cmd=sys.argv[1]
        # print(cmd)
        repo=sys.argv[2]
        repoacc=repo.replace('github.com','github.com.cnpmjs.org')
        os.system('cd '+target_path+'&&git clone ' +repoacc)
    else:
        print('加速器暂不支持其他git指令,请使用gitacc clone')
# if __name__ == '__main__':
#     acc()