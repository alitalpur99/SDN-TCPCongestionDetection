# """
# using dictionaries, take key as Chksum and Time as value (since dict keys can't be duplicated) 
# """


import datetime
from datetime import timedelta


""" For S1 """
time1=[]
t1=[]
c1=[]
chksum1=[]
dic1=dict()
with open("switch1-time.txt") as f1:
	for l1 in f1:
		l1=l1.strip()
		l1=l1.split(" ")
		t1.append(l1[0])
		c1.append(l1[1])
		# print l[1]
		time1=l1[0]
		chksum1=l1[1]
		dic1[chksum1]=time1

# print dic1, len(dic1)

# # ########################################################################################################################


""" For S2 """

time2=[]
chksum2=[]
t2=[]
c2=[]
dic2=dict()
with open("switch4-time.txt") as f2:
	for l2 in f2:
		l2=l2.strip()
		l2=l2.split(" ")
		t2.append(l2[0])
		c2.append(l2[1])
		# print l[3]
		time2=l2[0]
		chksum2=l2[1]
		dic2[chksum2]=time2
# print dic2, len(dic2)

# print t2#,len(t1)
# # #####################################################
# # '''COMPARING TWO DICTIONARIES'''
# dic=dict()
# open("s1s4keyok","w").close()
# with open("s1s4keyok","w+") as fkey:
# 	for k,v in dic1.items():
# 		for key,val in dic2.items():
# 			if k==key:
# 			# print "s1", k,v, "--", "S2", key,val
# 				fkey.write(str(k)+" "+ str(v)+" "+str(key)+" "+str(val))
# 				fkey.write("\n")

# # #########################################################
# # """ sorting dictionaries using Time values """

import operator
sorted_dic1 = sorted(dic1.items(), key=operator.itemgetter(1))
# print sorted_dic1, len(sorted_dic1)
sorted_dic2 = sorted(dic2.items(), key=operator.itemgetter(1))

# """print sorted dic1 and 2"""
open("sorteddic1","w").close()
with open("sorteddic1","w+") as ff:
	for i in range(len(sorted_dic1)):
		ff.write(str(sorted_dic1[i])+" "+ "\n")

open("sorteddic2","w").close()
with open("sorteddic2","w+") as ff:
	for i in range(len(sorted_dic2)):
		ff.write(str(sorted_dic2[i])+" "+ "\n")


# # ###########################################
# # """Print time of the S1"""
# # dic1_t= [x[1] for x in sorted_dic1]
# # # for i in range(len(dic1_t)):
# # # 	print dic1_t[i].split(":")[2]
# # """Print time of the S2"""
# # dic2_t= [x[1] for x in sorted_dic2]
# # # for i in range(len(dic2_t)):
# # # 	print dic2_t[i].split(":")[2]

# # # """ Get the time tuple as dic_t or chksum tuple as dic_v"""

dic2_t = [x[1] for x in sorted_dic2] # take teh time
dic2_v = [x[0] for x in sorted_dic2] # take the value / chksum
# # print dic2_v


open("sortedtupless1s4","w").close()

with open("sortedtupless1s4","w+") as sf:

	with open("sorteddic1") as df:

		for line in df:
			line=line.strip()
			for i in range(len(sorted_dic2)):
				if dic2_v[i] in line:
					"""	format of file: checksumofs4, timeofs4, chksumofs1,times1"""
					sf.write(str(dic2_v[i]) + " " +str(dic2_t[i])+" " +str(line))
					sf.write("\n")


times1=[]
times2=[]
t_s1=[]
diff=[]
with open("sortedtupless1s4") as f:
	
	datetimeFormat = '%H:%M:%S.%f' 
	for l in f:
		l=l.strip()
		l=l.split()
		times2.append(l[1]) # time of packetin at s2
		times1.append(l[3]) # time of packetin at s1

	# print times1
	for n in range(len(times1)):
		s=str(times1[n])
		a="'"
		b="')"
		for char in a:
			s=s.replace(char,"")
			for char in b:
				s=s.replace(char,"")
			t_s1.append(s)
		diff.append(datetime.datetime.strptime(times2[n],datetimeFormat)-datetime.datetime.strptime(t_s1[n],datetimeFormat))
		# print datetime.datetime.strptime(times2[n],datetimeFormat)-datetime.datetime.strptime(t_s1[n],datetimeFormat)
	# print t_s1
open("owd","w").close()
with open("owd","w+") as f:
	for i in range(len(diff)):
		t2_s=str(t_s1[i])  # take time of switch s1
		t2_time=t2_s.split(":")[2]
		# print t2_time

		if i<1:
			offset=t2_time
			print offset

		rel_time=float(t2_time) - float(offset)
		
		diff_s=str(diff[i])
		diff_sec=diff_s.split(":")[2]

		if str(diff[i]).startswith("-1"):
			f.write(str(t2_time)+" "+str('00.000000')+" "+str(rel_time))
			f.write("\n")
		else:
			f.write(str(t2_time)+" "+str(diff_sec)+" "+str(rel_time))
			f.write("\n")
# print diff


# '''checking for same key val in both dic, NOT WORKING'''
# # same=set(dic1.items()) & set(dic2.items())
# # print same, len(same)

###########################################################

#"""calculating  switch S4 IAT and saving in a  new file"""



time_s2=[]
iat=[]
iat_new=[]
with open("sortedtupless1s4") as f:
	for l in f:
		l=l.split(" ")
		time_s2.append(l[1])

## print type(time_s2)
		
datetimeFormat = '%H:%M:%S.%f'
for n in range(len(time_s2)):

	if  n>0:

		iat.append(datetime.datetime.strptime((time_s2[n]),datetimeFormat)-datetime.datetime.strptime(time_s2[n-1],datetimeFormat))

# print iat

open ("s4_iat","w").close()
with open("s4_iat","w+") as f:
	for i in range(len(time_s2)-1):
		iat1=str(iat[i])

		if iat1.startswith("-1") :
			#print "00.00"
			iat_new.append("00.00")
		
		else:
			iat_sec=iat1.split(":")[2]

			if float(iat_sec) > 0.086: # max value is this
				iat_new.append("00.00")

			else:	
				iat_new.append(iat_sec)	

		time2_string=str(time_s2[i+1])
		time2_string=time2_string.split(":")[2]
		f.write(str(time2_string)+" "+str(iat_new[i])+"\n")



# # iat=[]

# # open ("s4_iat","w+").close()
# # with open("s4_iat","w+") as f:
# # 	datetimeFormat = '%H:%M:%S.%f' 
# # 	for n in range(len(t2)):

# # 		if n>0:
# # 			iat.append(datetime.datetime.strptime(t2[n],datetimeFormat)-datetime.datetime.strptime(t2[n-1],datetimeFormat))
# # 	print max(iat)
# # 	for i in range(len(iat)):
	
# # 		iat_sec=str(iat[i])
# # 		iat_sec=iat_sec.split(":")[2]
# # 		time_s2_sec=str(t2[i+1])
# # 		time_s2_sec=time_s2_sec.split(":")[2]
# # 		f.write(str(time_s2_sec)+" "+ str(iat_sec)+"\n")