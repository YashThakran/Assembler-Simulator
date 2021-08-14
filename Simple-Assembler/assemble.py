import os

reg_list=['R0','R1','R2','R3','R4','R5','R6','FLAGS']
reg_address_list=['000','001','010','011','100','101','110','111']
typeA_list=['add','sub','mul','xor','or','and']
typeB_list=['mov','rs','ls']
typeC_list=['mov','div','not','cmp']
typeD_list=['ld','st']
typeE_list=['jmp','jlt','jgt','je']
bin_list=[]

def A(str st, str r1, str r2, str r3):
    if st=="add":
        return '00000'+'00'+r1+r2+r3
    else if st=='sub':
        return '00001'+'00'+r1+r2+r3
    else if st=='mul':
        return '00110'+'00'+r1+r2+r3
    else if st=='xor':
        return '01010'+'00'+r1+r2+r3
    else if st=='or':
        return '01011'+'00'+r1+r2+r3
    else if st=='and':
        return '01100'+'00'+r1+r2+r3
        
def B(str st, str r1, str r2):
    if st=="mov":
        return '00010'+r1+r2
    else if B=="rs":
        return '01000'+r1+r2
    else if st=="ls":
        return '01001'+r1+r2
    
def C(str st, str r1, str r2):
    if st=="mov":
        return '00011'+'00000'+r1+r2
    else if st=="div":
        return '00111'+'00000'+r1+r2
    else if st=="not":
        return "01101"+'00000'+r1+r2
    else if st=="cmp":
        return '01110'+'00000'+r1+r2

def D(str st, str r1, str mem_reg):
    if st=="ld":
        return '00100'+'000'+r1+mem_reg
    else if st=="st":
        return '00101'+'000'+r1+mem_reg
    
def E(str st,str mem_add):
    if st=="jmp":
        return '01111'+'000'+mem_add
    else if st=="jlt":
        return '10000'+'000'+mem_add
    else if st=="jgt":
        return '10001'+'000'+mem_add
    else if st=="je":
        return '10010'+'000'+mem_add
    
def F():
    return '10011'+'0000000000'

def check(ins):

    global bin_list
    global reg_list
    global typeA_list
    global typeB_list
    global typeC_list
    global typeD_list
    global typeE_list

    if len(ins)==1 and 'hlt' in ins:
        x=F()
        bin_list.append(x)
        return True
    else if len(ins)==4 and ins[0] in typeA_list:
        if ins[1] in reg_list and ins[2] in reg_list and ins[3] in reg_list:
            # x=A()
            bin_list.append(x)
            return True
    else if len(ins)==3 and ins[0] in typeB_list:
        if ins[1] in reg_list and (int(ins[2])>=0 or int(ins[2])<=255):
            #command for dec to bin to string
            # x=B()   
            bin_list.append(x)
            return True

    else if len(ins)==3 and ins[0] in typeC_list:
        if ins[1] in reg_list and ins[2] in reg_list:
            # x=C()
            bin_list.append(x)
            return True
    else if len(ins)==3 and ins[0] in typeD_list:
        if ins[1] in reg_list and (int(ins[2])>=0 or int(ins[2])<=255):
            #command for dec to bin to string
            # x=D()
            bin_list.append(x)
            return True

    else if len(ins)==2 and ins[0] in typeE_list:
        if (int(ins[1])>=0 or int(ins[1])<=255):
            #command for dec to bin to string
            # x=E()
            bin_list.append(x)
            return True


    return False



if __name__=='__main__':

    global bin_list

    f=open(r"sample.txt","r")

    l=[]

    for line in f:
        s=line.strip()
        lis=s.split()
        l.append(lis)

    line_count=0

    for st in l:
        err=check(st)
        line_count+=1
        if not err:
            print("Error at line ",line_count)
            break


    f.close()

