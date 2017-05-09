"""FOR PREPROCESSING AND SMOOTHING THE DELAY VALUES """


field1=[]
field3=[]
time=[]
with open("owd") as f:
	for l in f:
		l=l.split()
		

		field1.append(l[0])
		# field3.append(l[2])
		# only check if the time is non-normal
		if float(l[1])>=0.065:
			time.append("0.065")
		elif float(l[1])<=0.01865:
			time.append("0.01995")
		else:
			time.append(l[1])

# print time, max(time)

open("owd-new","w").close()

with open("owd-new","w") as wf:
	for n in range(len(time)):
		wf.write(str(field1[n])+" " +str(time[n])+"\n")
		#+" " + str(field3[n])+"\n")

########################################################################################



field1=[]
field3=[]
time=[]
with open("s4_iat") as f:
	for l in f:
		l=l.split()
		

		field1.append(l[0])
		# field3.append(l[2])
		# only check if the time is non-normal
		if float(l[1])>=0.02165:
			time.append("0.019065")
		# if float(l[1])>=0.065:
		# 	time.append("0.065")
		else:
			time.append(l[1])

# print time, max(time)

open("s4_iat-new","w").close()

with open("s4_iat-new","w") as wf:
	for n in range(len(time)):
		wf.write(str(field1[n])+" " +str(time[n])+"\n")
		#+" " + str(field3[n])+"\n")

########################################################################################
