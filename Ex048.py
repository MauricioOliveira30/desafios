s=0
ímp=0
for c in range (1,501):
    if c%3==0 and c%2==1:
        ímp+=1
        s+=c
print('O somatório dos {} valores é {}'.format(ímp,s))
