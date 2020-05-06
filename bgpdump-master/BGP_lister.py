import os
import subprocess
import re
import ipaddress
import json

def runProcess(exe):    
    p = subprocess.Popen(exe, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while(True):
        # returns None while subprocess is running
        retcode = p.poll() 
        line = p.stdout.readline()
        yield line
        if retcode is not None:
            break


def list_bgp(fle,dest_fldr,source_fldr):
	Date=source_fldr[-5:]
	
	dict_k={}
	file=dest_fldr+'/'+Date+'_BGP_records.json'
	l=[]
	
	cmd='./bgpdump '+source_fldr+'/'+fle
	
	cnt=1
	for line in runProcess(cmd.split()):
		
		l=(line.decode('utf-8')[:-1].split(','))
		if len(l)==1 and l[0]=="":
			cnt+=1
		
		k=0
		

		while k<len(l):
			
			temp_t=str(cnt)
		
			pl=l[k].find(': ')
			if pl!=-1:
				
				key=l[k][:pl]
				value=l[k][pl+2:]
				
				if key=="TIME":
					dict_k[temp_t]={}
					
				if dict_k.get(temp_t) is not None:
					dict_k[temp_t][key]=value
			else:
				#print("a")
				#print(l[k])
				if str(l[k]).isalpha():
					key=l[k]
					#print(key)
				elif '/' in str(l[k]):
					value=l[k]
					#print("a")
					if dict_k[temp_t].get(key) is None:
						dict_k[temp_t][key]=[value]
					else:
						#print(key)
						#temp=dict_k[temp_t].get(key)
						#temp=temp.append(value)
						#print(temp)
						dict_k[temp_t][key].append(value)
					#print(key+" :  "+value)
					#k+=1
				else:
					k+=1
					continue

			k+=1

	return file,dict_k

def bgp_caller():
	#os.system('cd bgpdump-master')
	source_fldr='/home/abhijit/Data_BGP'
	dest_fldr='/home/abhijit/Details_BGP'
	src_files=os.listdir(source_fldr)
	for fle in src_files:
		main_ext=source_fldr+"/"+fle
		files=os.listdir(main_ext) 
		for main in files:
			files,dict_k=list_bgp(main,dest_fldr,main_ext)
		with open(files, "w") as outfile:
			json.dump(dict_k, outfile) 


bgp_caller()
