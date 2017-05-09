#!/usr/bin/python

'''print the timestamps and checksum for the packet-in messages of Switch S1'''


from itertools import islice

import datetime
from datetime import timedelta
iat=[]
timestamps=[]
mins1=[]
sec1=[]
sec1_diff=[]
mins1_diff=[]
chksum1=[]
field=[]

#	FOR SWITCH S1

# Create and empty the result file
open('switch1-result.txt', 'w').close()

with open('switch1') as f:
	for line in f:
		line = line.rstrip()
		if line.startswith('2016') and 'OFPT_PACKET_IN' in line:
			line = line.strip()
			# join the next line to OFPT_PACKET_IN
			newline = line + ' '+ ''.join(islice(f,1)) 

			# check if this is packet from h1 as source port tp_src=42267
			if 'tp_src=42267' in newline: 
				with open('switch1-result.txt', 'a') as wfile:
					wfile.write("%s" %newline)	

with open('switch1-result.txt', 'r') as tfile:
	for l in tfile:
		l = l.rstrip().split(' ')
		
		### APPEND DUPLICATE CHECKSUMS		
		# chksum1.append(l[-1:])
		# field=l[1]
		# timestamps.append(field[:-1])	



		### DONOT APPEND DUPLICATE CHKSUMS
		if l[-1:] not in chksum1:
			chksum1.append(l[-1:])
			field=l[1]
			timestamps.append(field[:-1])	

	for n in range(len(timestamps)):
		timeFormat = '%H:%M:%S.%f' 
		# print timestamps[n]
		if n>0:

			# Calculate the IAT at switch1
			# print (datetime.datetime.strptime(timestamps[n],timeFormat)- datetime.datetime.strptime(timestamps[n-1],timeFormat))
			iat.append(datetime.datetime.strptime(timestamps[n],timeFormat) - datetime.datetime.strptime(timestamps[n-1],timeFormat))
			# print timestamps[n]


	# for i in range(len(sec1)):

		# # Calculate the difference of time (mins1 and sec1)
		# mins1_diff.append('{0:.6}'.format(float(mins1[i])-float(mins1[i-1])))
		# sec1_diff.append('{0:.6f}'.format(float(sec1[i])-float(sec1[i-1])))

# print sec1_diff
# Create and empty Time file 
open('switch1-time.txt', 'w').close()

with open('switch1-time.txt',"w+") as timef:
	
	for n in range(len(iat)):
		
		# timef.write(str(timestamps[n+1]) + " " + str(chksum1[n+1]) +" " + str(iat[n])  + "\n")
		timef.write(str(timestamps[n+1]) + " " + str(chksum1[n+1])+" " +str(iat[n]) +"\n")
		
	# for n in range(len(sec1_diff)):

		# if n<1:
		# 	sec1_diff[n]='0.000000'
		# 	mins1_diff[n]='0.0'

		# 	# append the file with difference of min and sec, and with checksum of packets
		# 	timef.write(str(timestamps[n]) + " " + str( mins1_diff[n]) + ":" 
		# 		+str(sec1_diff[n]) + " " + str(chksum1[n]) + "\n")
		
		# else:
		# 	# append the file with difference of min and sec, and with checksum of packets
		# 	timef.write(str(timestamps[n]) + "\t\t\t" + str( mins1_diff[n]) + ":" 
		# 		+str(sec1_diff[n]) + "\t\t\t" + str(chksum1[n]) + "\n")





#############################################################################################


'''TO see the UNIQUE ENTRIES IN S1 CHECKSUM'''
# seen1=[]
# uniq_S1 = [x for x in chksum1 if x not in seen1 and not seen1.append(x)]   
# print "Number of Unique Checksum entries in S1",len(uniq_S1) # 11364 (total = 12464)
# print"unique entries in S1 are: \n" seen1
# print len(uniq_b)

# dup=[]
# uni=[]
# # count=0
# for i,v in enumerate(chksum1):
# 	if v not in uni:
# 		uni.append(v)
# 	else:
# 		dup.append(v)
# 		print v,i
# 		# count+=1
# print len(dup)#, dup, len(uni)

#########################################################################################
## USE OF DICT TO FIND APPEND THE KEY: 'CHECKSUM' AND VAL: "TIME"

# c=[]
# time=[]
# dic=dict()
# i=0
# with open('switch1-result.txt', 'r') as tfile:
# 	for l in tfile:
# 		time.append(l[11:23])
# 		t=l[11:23] # Time
# 		# print len(l)
# 		c1=l.find('tcp_csum')
# 		c2=l.find(" ",c1)
# 		chksum=l[c1:c2]
# 		c.append(chksum)
# 		# print chksum
# 		dic[chksum]=t
# 		i+=1
# 		# if i==100: break
# print dic, len(dic)
# print len(time)
# print len(c)

'''can't use time as key, : problem since keys can not be duplicated, hence i used checksum as keys, but they also duplicated'''








################################################################################

'''TO GET THE VALUE OF CHECKSUM AS A STRING (replace [] brackets)'''
# x=[]
# i=0
# a="['"
# b="']"
# with open('switch1-result.txt') as rf1:
# 	for l in rf1:
# 		l=l.split()
# 		if i<1:
# 			# if "tcp_csum:ed2" is l[-1:]:
# 			x=l[-1:]
# 			print x
# 			x=str(x) 
# 			for char in a:
# 				x=x.replace(char, '')
# 				for char in b:
# 					x=x.replace(char,'')
# 			with open("cc","w+") as cf:
# 			# print x
# 				cf.write(x)
# 			i=i+1