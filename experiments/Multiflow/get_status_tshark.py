'''
CHANGE THE ORIGINAL WIRESHARK FILE TO ONLY DISPLAY THE NO, TIME & INFO COLUMNS
'''


import datetime
from datetime import timedelta



"""FOR SENDER H1, TAKE THE TIME VALUES"""

i1=0
count1=0
fields1=[]
time1=[]
with open('h1dump.txt','r') as f1:
	for line in f1:
		i1=i1+1
		line=line.split()
			
		# print line[8]
		if line[3]=='10.0.0.1':# and :
		# 	# line=line[4:]
			if line[11]=='57636' or line[10]=='57636'  or line[8]=='57636' or line[9]=='57636':
				# print line[1]
		 		time1.append(line[2])
		 		fields1.append(line[7:])

# 		# 		# print line
				count1 = count1+1
		## if i1>100: break
# # # # 			if line[6]=='55000':

# ## """GET THE SEQUENCE NUMBER"""

seq1=[]
for i in range(len(fields1)):
	# print fields1[i]
	string1= str(fields1[i])
 	s_start=string1.find("Seq")
 	s_end=string1.find("'",s_start)
 	# print s_start
 	# print s_end
	# print string1[s_start-1+1:s_end]
	seq1.append(string1[s_start-1+1:s_end])
print len(seq1)
print count1 #41378


open("h1-timeseq","w").close()
with open("h1-timeseq","w+") as h1f:
	for i in range(len(time1)):
		h1f.write(str(time1[i])+" "+str(seq1[i])+"\n")

# # # ############################# # ############################# # ############################# # ############################


# """FOR RECEIVER H4, TAKE TIME VALUES"""
i2=0
count2=0
time2=[]
fields2=[]
with open('h4dump.txt','r') as f2:
	for line in f2:
		i2=i2+1
		line=line.split()
			
		# print line[6:]
		if line[3]=='10.0.0.1':# and :
		# 	# line=line[4:]
			if line[10]=='57636' or line[11]=='57636'  or line[8]=='57636' or line[10]=='57636'or line[13]=='57636':
				# print line[4]
		 		time2.append(line[2])
		 		fields2.append(line[7:])
		# 		# print line
				count2 = count2+1
		# if i==110: break
# # # 			if line[6]=='55000':


## """GET THE SEQUENCE NUMBER"""

seq2=[]
for i in range(len(fields2)):
	# print fields1[i]
	string2= str(fields2[i])
 	s_start=string2.find("Seq")
 	s_end=string2.find("'",s_start)
 	# print s_start
 	# print s_end
	# print string2[s_start-1+1:s_end]
	seq2.append(string2[s_start-1+1:s_end])

print len(seq2)
print count2 # 41295

open("h4-timeseq","w").close()
with open("h4-timeseq","w+") as h4f:
	for i in range(len(time2)):

		h4f.write(str(time2[i])+" "+str(seq2[i])+"\n")

# # # ############################# # ########################## # ############################# # ############################

# """ write Time-Seq of both H1,H4 in a file"""
## Note: Some Seq numbers are repeated, so necessary to do line by line
timeseq=[]
time_h1=[]
time_h4=[]
seq_h1=[]
seq_h4=[]

with open("h4-timeseq") as f4:
	for l in f4:
		with open("h1-timeseq") as f1:
			l=l.strip()
			t2=l.split(" ")[0]
			s2=l.split(" ")[1]
			# print l
# 			for i in range(len(time2)):
			for line in f1:
				line =line.strip()
				t1=line.split(" ")[0]
				s1=line.split(" ")[1]


				# when sequence number of both hosts are equal append the time-seq values
				
				if s1==s2: 
					# print s2 seq time, s1 seq time
					timeseq.append(str(line)+ " "+ str(t2)+" "+ str(s2)+"\n")
					time_h1.append(t1)
					seq_h1.append(s1)
					time_h4.append(t2)
					seq_h4.append(s2)

print len(time_h1), len(timeseq)
open("h1h4timeseqok","w").close()
with open("h1h4timeseqok","w+") as wf:
	for n in range(len(timeseq)):
		## print timeseq[n]
		wf.write(str(timeseq[n]))
		
#################################################################################


# diff=[]
# with open("h1h4timeseqok") as file:
	
# 	for n in range(len(time2)):
		# print 'H1',time1[n], fields1[n]
		# print 'H4',time2[n], fields2[n]

		# diff.append(datetime.datetime.strptime(time2[n],timeFormat) - datetime.datetime.strptime(time1[n],timeFormat))
# 		file.write('H4'+' '+str(time2[n])+' '+str(fields2[n]))
# 		file.write('\n')
# 		file.write('H1'+' '+str(time1[n])+' '+ str(fields1[n]))
# 		file.write('\n')
# 		file.write(str(diff[n])+"\n")


# # # # ############################# # ####################### # ############################# # ############################


# """CREATE A FILE WITH TIME AND (H4-H1 DIFF = ONE-WAY DELAY)"""
one_way_delay=[]
timeFormat = '%H:%M:%S.%f'

for n in range(len(time_h4)):
	print time_h4[n], time_h1[n]
	one_way_delay.append(datetime.datetime.strptime(time_h4[n],timeFormat) - datetime.datetime.strptime(time_h1[n],timeFormat))

time1=[]
with open("h1h4timeseqok") as f:
	for line in f:
		line=line.strip()
		t1=line.split(" ")[0]
		# t2=line.split(" ")[2]
		time1.append(t1.split(":")[2])


open('tcpdump-timedelay','w').close()
with open('tcpdump-timedelay','w+') as file:
	for n in range(len(one_way_delay)):
		d=str(one_way_delay[n])
		delay=d.split(":")[2]
		if n >0:
			file.write(str(time1[n]+" "+str(delay)+"\n"))
		

		# for i in
		# diff = datetime.datetime.strptime(t2[line],timeFormat) - datetime.datetime.strptime(t1[line],timeFormat)
		# diff.append(datetime.datetime.strptime(t2[line],timeFormat) - datetime.datetime.strptime(t1[line],timeFormat))


# 			t1=t1.split(":")[2]
# 			# t2=t2.split(":")[2]
# 			print t1, diff

# 	total=0

# 	for n in range(len(time2)):

# 		t=str(time1[n])
# 		t=t.split(":")[2]
# 		# print t

# 		d=str(diff[n])
# 		d=d.split(":")[2]
# 		# print d

# 		if n>6:
# 			file.write(str(t)+" "+str(d) +"\n")

		# print time_diff
		# one_way_delay=str(time_diff)
		# one_way_delay=one_way_delay.split(":")[2]
		# print one_way_delay
		# time_diff = float(time2[n])-float(time1[n])
		# file.write(str(time2[n])+" "+str(time_diff))
		# file.write('\n')

		# if n<10418:
			# print sec
	
		# else:
			# print total
	
		# file.write(str(total)+" "+str(one_way_delay))
		# file.write('\n')

		# # when first time 59.99 sec achieved add 60 to it
		# if n>10418: 
		# 	total=float(sec)+60
		
		
		# 	# when second time 59.99 is reached, add 120 to it
		# 	if n>59941:
		# 		total=float(sec)+120