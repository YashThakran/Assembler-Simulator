

register_dict={"000":0000000000000000,"001":0000000000000000,"010":0000000000000000,"011":0000000000000000,"100":0000000000000000,"101":0000000000000000,"110":0000000000000000}

#file open in list f
f=[]

memory = ['0000000000000000' for i in range(256)]
for i in range(0,257):
    if f[i]!= '0000000000000000':
        memory[i]=f[i]

PC=0

halt=False

while(not halt):
    
    a=memory[PC]

    if a[:6]=='00000':
        add

    if a[:6]=='00001':
        sub

    if a[:6]=='00010':
        move imm
    
    if a[:6]=='00011':
        move reg

    if a[:6]=='00100':
        load

    if a[:6]=='00101':
        store

    if a[:6]=='00110':
        multiply

    if a[:6]=='00111':
        divide

    if a[:6]=='01000':
        right shift

    if a[:6]=='01001':
        left shift

    if a[:6]=='01010':
        exclusive or

    if a[:6]=='01011':
        or

    if a[:6]=='01100':
        and

    if a[:6]=='01101':
        invert

    if a[:6]=='01110':
        compare

    if a[:6]=='01111':
        unconditional jump

    if a[:6]=='10000':
        jump if less

    if a[:6]=='10001':
        jump if greater

    if a[:6]=='10010':
        jump if equal

    if a[:6]=='10011':
        halt
