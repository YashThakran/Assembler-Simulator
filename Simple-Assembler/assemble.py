if __name__=='__main__;:
	import os

	f=open(r"sample.txt",'r+')

	instruction_list=[]

	for line in f:
   		s=line.strip()
    	lis=s.split()
    	instruction_list.append(lis)

	for x in instruction_list:
		for sub in x:
		
		#conditions
	
	
	f.close()


