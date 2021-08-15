import os

#all instructions and addresses declared globally

reg_list=['R0','R1','R2','R3','R4','R5','R6']
reg_address_list=['000','001','010','011','100','101','110']
typeA_list=['add','sub','mul','xor','or','and']
typeB_list=['mov','rs','ls']
typeC_list=['mov','div','not','cmp']
typeD_list=['ld','st']
typeE_list=['jmp','jlt','jgt','je']
bin_list=[]
endpoint=True             #boolean to determine valid endpoint

def dectobin(num):               #function to convert decimal to binary
        if num >= 1:
            dectobin(num // 2)
        return num % 2 

def bintostr(n):                     #function to convert binary to 8-bit string
    q=dectobin(n)
    s=str(q)
    p=len(s)
    if p==8:
        return s
    elif p<8 and p>=0:
        return (8-p)*'0'+s


def A(st,r1,r2,r3):                               #function of type A to make a binary

    global reg_address_list

    if r1=='FLAGS':
        a='111'
    else:
        a=reg_address_list[int(r1[1])]
    if r2=='FLAGS':
        b='111'
    else:
        b=reg_address_list[int(r2[1])]
    if r3=="'FLAGS":
        c='111'
    else:
        c=reg_address_list[int(r3[1])]

    if st=="add":
        return '00000'+'00'+a+b+c
    elif st=='sub':
        return '00001'+'00'+a+b+c
    elif st=='mul':
        return '00110'+'00'+a+b+c
    elif st=='xor':
        return '01010'+'00'+a+b+c
    elif st=='or':
        return '01011'+'00'+a+b+c
    elif st=='and':
        return '01100'+'00'+a+b+c
        
def B(st,r1,r2):                                 #function of type B to make a binary

    global reg_address_list

    if r1=='FLAGS':
        a='111'
    else:
        a=reg_address_list[int(r1[1])]

    if st=="mov":
        return '00010'+a+r2
    elif B=="rs":
        return '01000'+a+r2
    elif st=="ls":
        return '01001'+a+r2
    
def C(st,r1,r2):                                #function of type C to make a binary

    global reg_address_list

    if r1=='FLAGS':
        a='111'
    else:
        a=reg_address_list[int(r1[1])]
    if r2=='FLAGS':
        b='111'
    else:
        b=reg_address_list[int(r2[1])]

    if st=="mov":
        return '00011'+'00000'+a+b
    elif st=="div":
        return '00111'+'00000'+a+b
    elif st=="not":
        return "01101"+'00000'+a+b
    elif st=="cmp":
        return '01110'+'00000'+a+b

def D(st,r1,mem_reg):                          #function of type D to make a binary

    global reg_address_list

    if r1=='FLAGS':
        a='111'
    else:
        a=reg_address_list[int(r1[1])]

    if st=="ld":
        return '00100'+'000'+a+mem_reg
    elif st=="st":
        return '00101'+'000'+a+mem_reg
    
def E(st,mem_add):                             #function of type E to make a binary
    if st=="jmp":
        return '01111'+'000'+mem_add
    elif st=="jlt":
        return '10000'+'000'+mem_add
    elif st=="jgt":
        return '10001'+'000'+mem_add
    elif st=="je":
        return '10010'+'000'+mem_add
    
def F():                                      #function of type F to make a binary
    return '10011'+'00000000000'

def check(ins):                         # function to check each instruction with fields

    global bin_list
    global reg_list
    global typeA_list
    global typeB_list
    global typeC_list
    global typeD_list
    global typeE_list
    global endpoint

    if ins==[]:
        endpoint=True
        return True

    if len(ins)==1 and ('hlt' in ins):
        x=F()
        bin_list.append(x)
        endpoint=False
        return True

    elif len(ins)==4 and (ins[0] in typeA_list):
        if (ins[1] in reg_list) and (ins[2] in reg_list) and (ins[3] in reg_list):
            x=A(ins[0],ins[1],ins[2],ins[3])
            bin_list.append(x)
            endpoint=False
            return True

    elif len(ins)==3 and (ins[0] in typeB_list):
        if (ins[1] in reg_list) and ins[2][0]=='$' and (int(ins[2][1:])>=0 or int(ins[2][1:])<=255):
            y=bintostr(int(ins[2][1:]))
            x=B(ins[0],ins[1],y)   
            bin_list.append(x)
            endpoint=False
            return True

    elif len(ins)==3 and (ins[0] in typeC_list):
        if (ins[1] in reg_list) and (ins[2] in reg_list):
            x=C(ins[0],ins[1],ins[2])
            bin_list.append(x)
            endpoint=False
            return True

    elif len(ins)==3 and (ins[0] in typeD_list):
        if (ins[1] in reg_list) and ins[2][0]=='$' and (int(ins[2][1:])>=0 or int(ins[2][1:])<=255):
            y=bintostr(int(ins[2][1:]))
            x=D(ins[0],ins[1],y)
            bin_list.append(x)
            endpoint=False
            return True

    elif len(ins)==2 and (ins[0] in typeE_list):
        if ins[1][0]=='$' and (int(ins[1][1:])>=0 or int(ins[1][1:])<=255):
            y=bintostr(int(ins[1][1:]))
            x=E(ins[0],y)
            bin_list.append(x)
            endpoint=False
            return True

    endpoint=True
    return False



if __name__=='__main__':

    f=open(r"sample.txt","r")

    l=[]

    for line in f:
        s=line.strip()                      #take each line and make a string
        lis=s.split()                     
        l.append(lis)                     #insert each instruction to a list

    line_count=0

    for j in range(len(l)):
        if l[j]==[]:
            line_count+=1
            continue
        correct=check(l[j])
        line_count+=1
        if not correct:                                            #check for syntax error
            print("Syntax Error at line ",line_count)
            break
        elif (endpoint==True and len(l[j:])>=1 and l[j]!=[]) or l.count(['hlt'])>1:            #checking more than 1 hlt statements
            print("Illegal use of statement 'hlt'. Error at line ",l.index(['hlt'])+1)
            correct=False
            break
        elif l[-1]!=['hlt']:                  #check for no hlt statement at last
            print("No endpoint detected.")
            correct=False
            break

    if correct:                     #if no errors, print the binary
        for i in bin_list:
            print(i,"\n")

    f.close()

