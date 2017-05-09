#!/usr/bin/python

'''print the timestamps and checksum for the packet-in messages of Switch S1/S2'''

#	FOR SWITCH S2
import S1_get_stats

import datetime
from datetime import timedelta
from itertools import islice

iat=[]
timestamps=[]
mins2=[]
sec2=[]
sec2_diff=[]
mins2_diff=[]
chksum2=[]
field=[]
j=0
#	FOR SWITCH S2

# Create and empty the result file
open('switch4-result.txt', 'w').close()

with open('switch4') as f:
	for line in f:
		line = line.rstrip()
		if line.startswith('2016') and 'OFPT_PACKET_IN' in line:
			line = line.strip()
			# join the next line to OFPT_PACKET_IN
			newline = line + ' '+ ''.join(islice(f,1)) 

			# check if this is packet from h1 as source port 57636
			if 'tp_src=57636' in newline: 
				with open('switch4-result.txt', 'a') as wfile:
					wfile.write("%s" %newline)	

with open('switch4-result.txt', 'r') as tfile:
	for l in tfile:
		l = l.rstrip().split(' ')
		# print l[1]
		
		### append mins2 and seconds and checksum of packets
		
		### APPEND DUPLICATE CHECKSUMS		
		# chksum1.append(l[-1:])
		# field=l[1]
		# timestamps.append(field[:-1])	



		### DONOT APPEND DUPLICATE CHKSUMS
		if l[-1:] not in chksum2:
			chksum2.append(l[-1:])
			field=l[1]
			timestamps.append(field[:-1])	
		
# print timestamps
# for i in range(len(timestamps1)):
	# timestamps.append(timestamps1[:-1])
	# print timestamps1[:-1]
	
	# for j in range(len(sec2)):
		
	# 	# Calculate the difference of time (mins2 and sec2)
	# 	mins2_diff.append('{0:.6}'.format(float(mins2[j])-float(mins2[j-1])))
	# 	sec2_diff.append('{0:.6f}'.format(float(sec2[j])-float(sec2[j-1])))

for n in range(len(timestamps)):
		datetimeFormat = '%H:%M:%S.%f' 
		# print timestamps[n]

		if n>0:

			# Calculate the IAT at switch2
			iat.append(datetime.datetime.strptime(timestamps[n],datetimeFormat)-datetime.datetime.strptime(timestamps[n-1],datetimeFormat))
			# a = datetime.strptime(timestamps[n],datetimeFormat)	

# print len(iat)
# print len(timestamps), len(chksum2)

open('switch4-time.txt', 'w').close()

# Save timestamps, IAT and checksum of switch2 in a file
with open('switch4-time.txt',"w+") as timef2:

	for n in range(len(chksum2)-1):
		
		timef2.write(str(timestamps[n+1]) + " " + str(chksum2[n+1]) +" " + str(iat[n])  + "\n")
# 		# timef2.write(str(timestamps[n+1]) + " " + str(chksum2[n+1]) + "\n")

# # # Create and empty Time file 
# open('switch2-time.txt', 'w').close()

# with open('switch2-time.txt',"w+") as timef2:
# 	for n in range(len(sec2_diff)):
		
# 		if n<1:
# 			sec2_diff[n]='0.000000'
# 			mins2_diff[n]='0.0'
# 			# append the file with difference of min and sec2, and with checksum of packets
# 			timef2.write(str(timestamps[n]) + " " + str(mins2_diff[n]) + "."
# 		 	+str(sec2_diff[n]) + " " + str(chksum2[n]) + "\n")		

# 		else:
# 			# append the file with difference of min and sec2, and with checksum of packets
# 			timef2.write(str(timestamps[n]) + " " + str(mins2_diff[n]) + "."
# 				+str(sec2_diff[n]) + " " + str(chksum2[n]) + "\n")		


		
########################################################
#Calculation of ONE WAY DELAY (between Switch1 - to - Swithc2)

time1=list()
time2=list()
delay=list()

# Open the switch1 time file, and append the time
with open('switch1-time.txt','r') as tf1:
	for l in tf1:
		l=l.split(" ")
		# print l[3]
		# print len(l)
		time1.append(l[0])
# print time1
# Open the switch2 time file, and append the timestamps
time_new=[]
with open('switch4-time.txt','r') as tf2:
	for m in tf2:
		m=m.split(" ")
		time2.append(m[0])
# with open('switch4-time.txt','r') as tf2:
# 	for g in tf2:
# 		g=g.split('\t')
# 		g=g[0].split('.')
# 		# print g[0]
# 		time_new.append(g[0])
# print time2
# Create and empty the One way delay file for switch2
open('switch4-delay.txt','w').close()

with open('switch4-delay.txt','w+') as df:
	datetimeFormat = '%H:%M:%S.%f' 
	print len(time1), len(time2),len(chksum2)
	for n in range(len(time2)):

		# Calculate the One-way Delay
		delay.append(datetime.datetime.strptime(time2[n], datetimeFormat) - datetime.datetime.strptime(time1[n],datetimeFormat))
		# print delay
		df.write(str((datetime.datetime.strptime(time2[n], datetimeFormat) - datetime.datetime.strptime(time1[n],datetimeFormat))))
		df.write(" "+str(time2[n])+" "+ str(time1[n])+" "+str(S1_get_stats.chksum1[n+1]) + " "+str(chksum2[n+1])+"\n")
		# df.write("\n")
# print len(time1),len(time2), len(chksum2)
# Create an empty file, to append Timesatmps, Checksum, IAT and One-way delay
open('switch4-all.txt','w').close()

with open('switch4-all.txt','w+') as cf:
	
	cf.write('S1-time' + ' ' + 'S2-time' + ' ' + 'IAT-S2'+' '+'Delay-S2'+' ' + 'S1-chksum'+' '+'S2-chksum'+ '\n')
	for n in range(len(time2)):
		# if S1_get_stats.chksum1[n] == chksum2[n]:

		# data = n.split(" ")
		# print '{0[0]:>15}{0[1]:>50}'.format(data)

		# data = str(time1[n+1])+ " " + str(time2[n+1]) + " " + str(iat[n+1]) + " " +  str(delay[n+1]) + " " +  str(S1_get_stats.chksum1[n+2]) + " " + str(chksum2[n+2]) + ("\n")
		# data=data.split(' ')
		# cf.write('{0[0]:15}{0[1]:15}{0[2]:35}{0[3]:25}{0[4]:25}{0[5]:>25}'.format(data))
		# print delay[n]		

		cf.write(str(time1[n]) + '\t'  + str(time2[n]) + '\t' + str(iat[n]) + '\t' +str(delay[n]) + '\t'
			+ str(S1_get_stats.chksum1[n])+ '\t\t' + str(chksum2[n])+'\n')


# print delay
# def get_sec(time_str):
#     h, m, s = time_str.split(':')
#     tg= int(h) * 3600 + int(m) * 60 + int(s)

# for i in range(len(time_new)):
# 	 get_sec(time_new[i])







#############################################################################################

'''TO CHECK DUPLICATE ENTRIES IN S2 CHECKSUM'''
# seen2=[] 
# uniq_S2 = [x for x in chksum2 if x not in seen2 and not seen2.append(x)]   
# print "Number of Unique Checksum entries in S1", len(uniq_S2) # 11352 (total = 12450)




# dup=[]
# uni=[]

# for i,v in enumerate(chksum2):
# 	if v not in uni:
# 		uni.append(v)
# 	else:
# 		dup.append(v)
		# print v,i
# print dup, len(dup), len(uni)
# print len(chksum2), len(timestamps)
