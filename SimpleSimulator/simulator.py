

register_dict={"000":0000000000000000,"001":0000000000000000,"010":0000000000000000,"011":0000000000000000,"100":0000000000000000,"101":0000000000000000,"110":0000000000000000}

#file open in list f
f=[]

memory = ['0000000000000000' for i in range(256)]
for i in range(0,256):
    if f[i]!= '0000000000000000':
        memory[i]=f[i]

PC=0
flag='0000000000000000'

halt=False

def bintodec(binary):




def dectobin(dec):





while(not halt):
    
    a=memory[PC]

    if a[:5]=='00000':
        flag='0000000000000000'
        sum=bintodec(a[10:13])+bintodec(a[13:16])
        register_dict[a[7:10]]=dectobin(sum)
        PC=PC+1

    if a[:5]=='00001':
        sub

    if a[:5]=='00010':
        move imm
    
    if a[:5]=='00011':
        move reg

    if a[:5]=='00100':
        load

    if a[:5]=='00101':
        store

    if a[:5]=='00110':
        multiply

    if a[:5]=='00111':
        divide

    if a[:5]=='01000':
        right shift

    if a[:5]=='01001':
        left shift

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
        halt