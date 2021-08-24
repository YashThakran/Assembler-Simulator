

register_dict={"000":0000000000000000,"001":0000000000000000,"010":0000000000000000,"011":0000000000000000,"100":0000000000000000,"101":0000000000000000,"110":0000000000000000,"111":0000000000000000}

#file open in list f
f=[]

memory = ['0000000000000000' for i in range(256)]
for i in range(0,256):
    if f[i]!= '0000000000000000':
        memory[i]=f[i]

PC=0

halt=False

def bintodec(binary):




def dectobin(dec):





while(not halt):
    
    a=memory[PC]

    if a[:5]=='00000':
        register_dict['111']='0000000000000000'
        sum=bintodec(a[10:13])+bintodec(a[13:16])
        binsum=dectobin(sum)
        if len(binsum)>16:
            binsum=binsum[-16:]
            register_dict['111']='0000000000001000'
        register_dict[a[7:10]]=binsum
        PC=PC+1

    if a[:5]=='00001':
        register_dict['111']='0000000000000000'
        if bintodec(a[13:16]) > bintodec(a[10:13]):
            register_dict[a[7:10]]='0000000000000000'
            register_dict['111']='0000000000001000'
            PC=PC+1
        else:
            diff=bintodec(a[10:13])+bintodec(a[13:16])
            register_dict[a[7:10]]=dectobin(diff)
            PC=PC+1

    if a[:5]=='00010':
        register_dict['111']='0000000000000000'
        register_dict[a[5:8]]='00000000'+a[8:16]
        PC=PC+1
    
    if a[:5]=='00011':
        register_dict[a[10:13]]=register_dict[a[13:16]]
        PC=PC+1
        register_dict['111']='0000000000000000'

    if a[:5]=='00100':
        register_dict['111']='0000000000000000'
        register_dict[a[5:8]]=memory[int(a[-8:],2)]
        PC=PC+1

    if a[:5]=='00101':
        register_dict['111']='0000000000000000'
        memory[int(a[-8:],2)]=register_dict[a[5:8]]
        PC=PC+1

    if a[:5]=='00110':
        register_dict['111']='0000000000000000'
        mul=bintodec(a[10:13])*bintodec(a[13:16])
        binmul=dectobin(mul)
        if len(binmul)>16:
            binmul=binmul[-16:]
            register_dict['111']='0000000000001000'
        register_dict[a[7:10]]=binmul
        PC=PC+1

    if a[:5]=='00111':
        register_dict['111']='0000000000000000'
        register_dict['000']=bintodec(a[10:13])//bintodec(a[13:16])
        register_dict['001']=bintodec(a[10:13])%bintodec(a[13:16])
        PC=PC+1

    if a[:5]=='01000':
        register_dict['111']='0000000000000000'
        rs=bintodec(register_dict[a[5:8]])>>int(a[8:],2)
        register_dict[a[5:8]]=dectobin(rs)
        PC=PC+1

    if a[:5]=='01001':
        register_dict['111']='0000000000000000'
        ls=bintodec(register_dict[a[5:8]])<<int(a[8:],2)
        register_dict[a[5:8]]=dectobin(ls)
        PC=PC+1

    if a[:5]=='01010':
        exclusive or

    if a[:5]=='01011':
        or

    if a[:5]=='01100':
        and

    if a[:5]=='01101':
        invert

    if a[:5]=='01110':
        compare

    if a[:5]=='01111':
        unconditional jump

    if a[:5]=='10000':
        jump if less

    if a[:5]=='10001':
        jump if greater

    if a[:5]=='10010':
        jump if equal

    if a[:5]=='10011':
        halt=True