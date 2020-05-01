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
	#print(Date)
	dict_k={}
	file=dest_fldr+'/'+Date+'_BGP_records.json'
	l=[]
	#ip_list={}
	cmd='./bgpdump '+source_fldr+'/'+fle
	#print(cmd)
	for line in runProcess(cmd.split()):
		l=(line.decode('utf-8')[:-1].split(','))
		k=0
		#print(len(l))
		while k<len(l):
			#print(l[k])	
			pl=l[k].find(': ')
			if pl!=-1:
				#k+=1
				#continue
				key=l[k][:pl]
				value=l[k][pl+2:]
				#print(value)
				if key=='TIME':
					temp_t=value[-8:]
					#print(value[-8:])
					dict_k[value[-8:]]={}
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
	source_fldr='/home/$user$/Data_BGP'
	dest_fldr='/home/$user$/Details_BGP'
	src_files=os.listdir(source_fldr)
	for fle in src_files:
		main_ext=source_fldr+"/"+fle
		files=os.listdir(main_ext) 
		for main in files:
			files,dict_k=list_bgp(main,dest_fldr,main_ext)
		with open(files, "w") as outfile:
			json.dump(dict_k, outfile) 


bgp_caller()
