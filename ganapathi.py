import time
for i in range(5):
    time.sleep(1)
    print('    '+' '*(5-i)+'*'*(2*i+1))
for l in range (5):
    time.sleep(1)
    if l==0:
        print('*'*19)
    elif l==2:
        print(' '*l+'*'*(l+1)+'  '+'*'+'   '+'*'+' '*2+'*'*(l+1))
    else:
        print(' '*(l)+'*'*(5-l)+' '*9+'*'*(5-l))
for j in range(5,-1,-1):
    time.sleep(1)
    if j==0:
        print('    '+' '*(5-j)+'*'*(2*j+1))
    else:
        print(' '*(5-j)+'    '+'*'+' '*(2*j-1)+'*')
for k in range(5):
    time.sleep(1)
    print('     '+' '*(5-k-2)+'*'+' '+'*')
for a in range(2,0,-1):
    time.sleep(1)
    print('     '+' '+'*'*a)

