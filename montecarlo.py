import random

N = 10
def inChk(x,y):
    if x*x+y*y <= 0.5**2:
        return True
    else:
        return False
for i in range(7):
    n_in=0
    j=0
    while j<N:
        x = random.random()-0.5
        y = random.random()-0.5
        if inChk(x,y)==True:
            n_in += 1
        j+=1    
    pi = 4*n_in/N
    print("サンプル{:>8}        円の内側の数：{:>8} πの近似値：{:<10}".format(N,n_in,pi))
    N*=10
