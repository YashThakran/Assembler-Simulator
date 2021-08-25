import matplotlib.pyplot as mlt
import sys

register_dict={"000":'0000000000000000',"001":'0000000000000000',"010":'0000000000000000',"011":'0000000000000000',"100":'0000000000000000',"101":'0000000000000000',"110":'0000000000000000',"111":'0000000000000000'}

files=open('inputfile.txt','w')
files.truncate(0)
for line in sys.stdin:
    files.write(line)
files.close()
files=open('inputfile.txt','r')
f=files.read().splitlines()
h=0
while (h<len(f)):
    if(f[h][-1]=='\n'):
        f[h]=f[h][0:-1]
    h=h+1


memory = ['0000000000000000' for i in range(256)]
for i in range(0,256):
    if f[i]!= '0000000000000000':
        memory[i]=f[i]

PC=0
cycle=0
data=[]

halt=False

def bintodec(binary):
    g=int(binary,2)
    return (g)

def dectobin(dec):
    j=bin(dec)[2:]
    while len(j)<16:
        j='0'+j
    return j



while(not halt):
    
    a=memory[PC]
    data.append([cycle,PC])
    

    if a[:5]=='00000':
        register_dict['111']='0000000000000000'
        sum=bintodec(a[10:13])+bintodec(a[13:16])
        binsum=dectobin(sum)
        if len(binsum)>16:
            binsum=binsum[-16:]
            register_dict['111']='0000000000001000'
        register_dict[a[7:10]]=binsum
        PC=PC+1
        cycle=cycle+1

    if a[:5]=='00001':
        register_dict['111']='0000000000000000'
        if bintodec(a[13:16]) > bintodec(a[10:13]):
            register_dict[a[7:10]]='0000000000000000'
            register_dict['111']='0000000000001000'
            PC=PC+1
            cycle=cycle+1
        else:
            diff=bintodec(a[10:13])+bintodec(a[13:16])
            register_dict[a[7:10]]=dectobin(diff)
            PC=PC+1
            cycle=cycle+1

    if a[:5]=='00010':
        register_dict['111']='0000000000000000'
        register_dict[a[5:8]]='00000000'+a[8:16]
        PC=PC+1
        cycle=cycle+1
    
    if a[:5]=='00011':
        register_dict[a[10:13]]=register_dict[a[13:16]]
        PC=PC+1
        cycle=cycle+1
        register_dict['111']='0000000000000000'

    if a[:5]=='00100':
        data.append([cycle,int(a[-8:],2)])
        register_dict['111']='0000000000000000'
        register_dict[a[5:8]]=memory[int(a[-8:],2)]
        PC=PC+1
        cycle=cycle+1

    if a[:5]=='00101':
        data.append([cycle,int(a[-8:],2)])
        register_dict['111']='0000000000000000'
        memory[int(a[-8:],2)]=register_dict[a[5:8]]
        PC=PC+1
        cycle=cycle+1

    if a[:5]=='00110':
        register_dict['111']='0000000000000000'
        mul=bintodec(a[10:13])*bintodec(a[13:16])
        binmul=dectobin(mul)
        if len(binmul)>16:
            binmul=binmul[-16:]
            register_dict['111']='0000000000001000'
        register_dict[a[7:10]]=binmul
        PC=PC+1
        cycle=cycle+1

    if a[:5]=='00111':
        register_dict['111']='0000000000000000'
        register_dict['000']=bintodec(a[10:13])//bintodec(a[13:16])
        register_dict['001']=bintodec(a[10:13])%bintodec(a[13:16])
        PC=PC+1
        cycle=cycle+1

    if a[:5]=='01000':
        register_dict['111']='0000000000000000'
        rs=bintodec(register_dict[a[5:8]])>>int(a[8:],2)
        register_dict[a[5:8]]=dectobin(rs)
        PC=PC+1
        cycle=cycle+1

    if a[:5]=='01001':
        register_dict['111']='0000000000000000'
        ls=bintodec(register_dict[a[5:8]])<<int(a[8:],2)
        register_dict[a[5:8]]=dectobin(ls)
        PC=PC+1
        cycle=cycle+1

    if a[:5]=='01010':
        exclusive or
        cycle=cycle+1

    if a[:5]=='01011':
        or
        cycle=cycle+1

    if a[:5]=='01100':
        and
        cycle=cycle+1

    if a[:5]=='01101':
        invert
        cycle=cycle+1

    if a[:5]=='01110':
        compare
        cycle=cycle+1

    if a[:5]=='01111':
        unconditional jump
        cycle=cycle+1

    if a[:5]=='10000':
        jump if less
        cycle=cycle+1

    if a[:5]=='10001':
        jump if greater
        cycle=cycle+1

    if a[:5]=='10010':
        jump if equal
        cycle=cycle+1

    if a[:5]=='10011':
        halt=True
        cycle=cycle+1

    PC=bin(PC)[2:]
    while len(PC)<8:
        PC='0'+PC



    print(PC+" "+register_dict['000']+" "+register_dict['001']+" "+register_dict['010']+" "+register_dict['011']+" "+register_dict['100']+" "+register_dict['101']+" "+register_dict['110']+" "+register_dict['111'])
    

x,y=zip(*data)
mlt.scatter(x,y)
mlt.savefig('bonus.png')