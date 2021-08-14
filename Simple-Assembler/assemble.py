import os

reg_list=['R0','R1','R2','R3','R4','R5','R6','FLAGS']
typeA_list=['add','sub','mul','xor','or','and']
typeB_list=['mov','rs','ls']
typeC_list=['mov','div','not','cmp']
typeD_list=['ld','st']
typeE_list=['jmp','jlt','jgt','je']
bin_list=[]

def check(ins):

    global bin_list
    global reg_list
    global typeA_list
    global typeB_list
    global typeC_list
    global typeD_list
    global typeE_list

    if len(ins)==1 and 'hlt' in ins:
        x=F('hlt')
        bin_list.append(x)
        return True
    else if len(ins)==4 and ins[0] in typeA_list:
        if ins[1] in reg_list and ins[2] in reg_list and ins[3] in reg_list:
            x=A(ins[0],ins[1],ins[2],ins[3])
            bin_list.append(x)
            return True
    else if len(ins)==3 and ins[0] in typeB_list:
        if ins[1] in reg_list and (int(ins[2])>=0 or int(ins[2])<=255):
            #command for dec to bin to string
            x=B()   
            bin_list.append(x)
            return True

    else if len(ins)==3 and ins[0] in typeC_list:
        if ins[1] in reg_list and ins[2] in reg_list:
            x=C(ins[0],ins[1],ins[2])
            bin_list.append(x)
            return True
    else if len(ins)==3 and ins[0] in typeD_list:
        if ins[1] in reg_list and (int(ins[2])>=0 or int(ins[2])<=255):
            #command for dec to bin to string
            x=D()
            bin_list.append(x)
            return True

    else if len(ins)==2 and ins[0] in typeE_list:
        if (int(ins[1])>=0 or int(ins[1])<=255):
            #command for dec to bin to string
            x=E()
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

